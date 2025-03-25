import json 
import os
from collections.abc import Iterable
from urllib.parse import urlsplit, urlunsplit
from datetime import datetime
from configparser import ConfigParser
import bs4
import tldextract
from bs4 import BeautifulSoup
from tqdm import tqdm
from tabulate import tabulate 
from crawlfish.crawler.download_image import download_image 
from crawlfish.crawler.download_static_code_file import download_static_code_file
from crawlfish.http import get_url
from crawlfish.crawlfish_utils import check_file ,check_folder
from crawlfish.html  import ensure_soup , get_element_text
from .get_base_url import get_base_url
from .get_url_parts import get_url_parts
from .url_to_folder_name import url_to_folder_name
from .extract_file_info_from_url import extract_file_info_from_url
 

PAGE_REPORT_STRING = """
======================================================================================
		  WEB PAGE REPORT
		 `````````````````
{}
======================================================================================
		
	Metadata 
{}

	Urls stats
{}

	Static data
{}

============================================

"""

DATA_NOT_FOUND = "NULL"

 

class WebpageReport:
	'''
	To be used as a container for data obtained after exloring one webpage
	Contains mostly links  and metadata 

	Parameters
	----------
	url:str
		The url of the webpage 
	title:str
		The title of the webpage 
	css_urls:Iterable 
		A list containing urls to css files
	js_urls:Iterable 
		A list containing urls to Javascript files 
	image_urls:Iterable
		A list containing urls to image files 
	css_tags:Iterable 
		A list containing css bs4.Tag  instances that represent <style> tags
	js_tags:Iterable 
		A list containing  bs4.Tag  instances that represent Javascript <script> tags
	json_tags:Iterable
		A list containing  bs4.Tag  instances that represent JSON <script> tags
	metadata:dict 
		A dictionary object containing the page's metadata info { key:value ... }
	other_site_urls:Iterable
		A list of urls to other websites 
	same_site_urls:Iterable 
		A list of urls found on the webpage that lead to pages of the same website
	soup:BeautifulSoup 
		A bs4.BeautifulSoup instance of the webpage's code 
	get_function:FunctionType
		A function that takes a url as an argument and returns a request.Response object 
	html:str
		The html code of the webpage 

	'''
	def __init__(
		self ,
		url:str ,
		title:str =DATA_NOT_FOUND,
		css_urls:Iterable = [] ,
		js_urls:Iterable = [] , 
		image_urls:Iterable=[],
		css_tags:Iterable = [] ,
		js_tags :Iterable= [] ,
		json_tags:Iterable = [],
		metadata:dict = {},
		other_site_urls:Iterable=[] , 
		same_site_urls:Iterable = [] ,
		soup:BeautifulSoup =None, 
		get_function = get_url,
  		html ='' 
  		):
		tld_result = tldextract.extract(url)
		self.domain = tld_result.domain
		self.url = url
		self.base_url  = get_base_url(url)
		self.soup = soup
		self.get_function = get_function
		self.html = ''
		self.elements_processed = 0
		if soup:
			self.html = soup.prettify()
			self.elements_processed = len(soup.find_all())
		else:
			self.soup = bs4.BeautifulSoup('' ,'html.parser')
		self.css_urls  = css_urls
		self.js_urls = js_urls
		self.image_urls = image_urls
		self.css_tags = css_tags 
		self.js_tags = js_tags 
		self.json_tags = json_tags
		self.title = title 
		self.metadata = meta data
		self.same_site_urls = same_site_urls
		self.split_url = urlsplit(url)
		self.network_location = self.split_url.netloc
		self.discovered_urls = []
		self.all_site_urls = []
		self.other_site_urls = other_site_urls
		self.internal_css_code ={}
		self.external_css_code ={}
		self.internal_js_code ={}
		self.external_js_code = {} 
		self.image_data = {}
		self.internal_json_code = {}
		self.already_downloaded_static = {}
		self.all_static_urls = self.image_urls + self.js_urls + self.css_urls
		self.all_static_data = {} # all static data . images, js , css
		self.DiscoverMoreSameSiteLinks()
		self.ExtractInternalCode()


	def DiscoverMoreSameSiteLinks(self):
		'''Looks for possible undiscovered urls of the same website '''
		discovered_urls = self.discovered_urls
		for url in self.same_site_urls:
			parts = get_url_parts(url)
			for i in parts :
				if not i in self.same_site_urls and not i in discovered_urls:
					discovered_urls.append(i)
		self.discovered_urls =  discovered_urls  
		print("Discovered {} possible same site  links ".format(len(self.discovered_urls)))
		self.all_site_urls = self.discovered_urls + self.same_site_urls

	def as_text(self):
		'''Returns this class' data in text form '''
		return self.__repr__()

	def as_dict(self  ):
		''' Returns the page data info as a dict object 

		'''
		data = {

				"static_stats":{ 
					'js_tags':len(self.js_tags),
					'css_tags':len(self.css_tags),
					'js_urls':len(self.js_urls),
					'css_urls':len(self.css_urls),
					'image_urls':len(self.image_urls),
					'json_tags':len(self.json_tags),
					"elements_processed":self.elements_processed,
						},
				"metadata":self.metadata,
				"urls":{
					"base_url":self.base_url,
					"network_location":self.network_location,
					"same_site_links":len(self.same_site_urls),
					"discovered_urls":len(self.discovered_urls),
					"other_site_urls":len(self.other_site_urls),
				},

				}

			 
		
		return data 

	def save_to_config_file(self , file:str ,encoding:str='utf-8'):
		''' Save the page report data in config  file using configparser
		Parameters
		----------
		file:str
			The name of the file where the data will be saved
		encoding:str
			The encoding to use during file read and write 

		Returns
		-------
		None 
		'''
		print("Saving Web page report to CONFIG file {} -------- ".format(file) , end = '')
		check_file(file)
		cp =ConfigParser()
		as_dict = self.as_dict()

		for title,data in as_dict.items():
			cp[title] = {}
			for k , v in data.items():
				cp[title][k] = str(v)
		with open(file , 'w' ,encoding =encoding) as f:
			cp.write(f)
		print("DONE !")



	def save_to_json_file(self , file:str, ensure_ascii:bool = False  ,
					 indent:int = 4 , encoding:str = "utf-8"):
		''' Saves this class' information in to a json file 

		Parameters
		----------
		file:str
			The name of the file where the data will be saved
		ensure_ascii:bool
			Ensures ascii in the json file 
		indent:int
			The indentation to use in the JSON file 
		encoding:str
			The encoding to use during file read and write 
		
		Returns
		-------
		None 
		'''
		print("Saving Web page report to JSON file {} -------- ".format(file) , end = '')
		to_write = self.as_dict()
		with open(file ,"w" ,encoding = encoding) as f:
			json.dump(to_write ,f  ,ensure_ascii=ensure_ascii, indent=indent)

		print("DONE")


	def save_to_text_file(self, file:str ,encoding:str = 'utf-8' ):
		''' Saves this class' information in to a text file

		Parameters
		----------
		file:str
			The name of the file where the data will be saved
		encoding:str
			The encoding to use during file read and write 
		
		Returns
		-------
		None 
		'''
		print("Saving Web page report to TEXT file {} -------- ".format(file) , end = '')
		check_file(file)
		data = self.as_text()
		with open(file , "w" ,encoding = encoding) as f:
			f.write(data)
		print("DONE")



	def ExtractInternalCode(self):
		''' Extract the code from css and js related tags '''
		print("Extracting JS internal code --- " , end ='')
		for tag in self.js_tags:
			code = get_element_text(tag)
			tag_id = "script_tag_{}.js".format(self.js_tags.index(tag))
			self.internal_js_code[tag_id] = code 
		print("DONE")
		print("Extracting CSS internal code --- " , end ='')
		for tag in self.css_tags:
			code = get_element_text(tag)
			tag_id = "script_tag_{}.css".format(self.css_tags.index(tag))
			self.internal_css_code[tag_id] = code 
		print("DONE")
		print("Extracting JSON code ------------" , end = '')
		for tag in self.json_tags:
			code = get_element_text(tag)
			tag_id = "script_tag_{}.json".format(self.json_tags.index(tag))
			self.internal_json_code[tag_id] = code 
		print("DONE")

	def FetchExternalCode(self , to_fetch = ["js" , "css"]):
		'''Download and store all external static  code

		Parameters
		----------
		to_fetch:Iterable 
			A list of the static file types to fetch 

		Returns
		-------
		None 

		'''
		if 'js' in to_fetch:
			self.FetchExternalJS()
		if 'css' in to_fetch:
			self.FetchExternalCSS()
		
	def FetchExternalCSS(self):
		"""Fetches external CSS code """
		for url in tqdm(self.css_urls ,"Fetching external CSS--"):
			file_name =extract_file_info_from_url(url)[0] 
			if file_name in self.already_downloaded_static:
				# dont download 
				# add the data 
				self.external_css_code[file_name] = self.already_downloaded_static[file_name]
				continue
			content ,base_name = download_static_code_file( url  , self.get_function , save_to_file = False)
			if not content.strip():
				continue
			self.external_css_code[base_name] = content

	def FetchExternalJS(self):
		"""Fetches external JS code"""
		for url in tqdm(self.js_urls ,"Fetching external Javascript--"):
			file_name =extract_file_info_from_url(url)[0] 
			if file_name in self.already_downloaded_static:
				# dont download 
				# add the data 
				self.external_js_code[file_name] = self.already_downloaded_static[file_name]
				continue
			base_name , content= download_static_code_file( url  , self.get_function ,save_to_file = False)
			if not content.strip():
				continue
			self.external_js_code[base_name] = content



	def FetchImages(self):
		''' Gets and saves the images in the image_utls attribute 

		Returns
		-------
		None

		'''
		for url in tqdm(self.image_urls , "Fetching {} images --- ".format(len(self.image_urls))):
			file_name =extract_file_info_from_url(url)[0] 
			if file_name in self.already_downloaded_static:
				# dont download 
				# add the data 
				self.image_data[file_name] = self.already_downloaded_static[file_name]
				continue
			base_name ,data = download_image(url , self.get_function , save_to_file = False)
			self.image_data[base_name] = data

	def save_images(self , output_folder:str = os.getcwd()):
		'''Saves the downloaded image data to files in the specified output folder 

		Parameters
		----------
		output_folder:str
			The folder where to save the image files 

		Returns
		-------
		None

		'''
		for base_name , data in tqdm(self.image_data.items() , "Downloading {} image(s)".format(len(self.image_data.keys()))):
			file = os.path.join(output_folder , 'images/' + base_name)
			if not check_file(file):continue
			with open(file , 'wb') as f:
				f.write(data)

	def save_static_code(self , file_code_dict:dict ,
						encoding:str ='utf-8' ,
						tqdm_message:str = "Saving static code"):
		'''Saves static code in the file_code_dixt dictionary into files

		Parameters
		----------
		file_code_dict:dict
			The file and data information in the format { filename:data ..... } 
		encoding:str
			The encoding to use during file read and write 
		tqdm_message:str
			The progress bar message	

		Returns
		-------
		None 

		'''
		for file ,code in tqdm(file_code_dict.items() , tqdm_message):
			if not check_file(file):
				continue
			with open(file, "w" , encoding=encoding) as f:
				f.write(code)

	def save_js_code(self , output_folder = os.getcwd() ,encoding = "utf-8"):
		''' Save javascript into files

		Parameters
		----------
		encoding:str
			The encoding to use during file read and write
		output_folder:str
			The folder where to save the JS files   

		Returns
		-------
		None 

		'''
		external_code_folder = os.path.join(output_folder ,"js/external")
		internal_code_folder = os.path.join(output_folder ,"js/internal")
		external_file_code_dict = {  os.path.join(external_code_folder , base_name):code for base_name,code in self.external_js_code.items()  }
		internal_file_code_dict = {  os.path.join(internal_code_folder , base_name):code for base_name,code in self.internal_js_code.items()  }
		self.save_static_code(external_file_code_dict , tqdm_message = "Saving external JS code ")
		self.save_static_code(internal_file_code_dict, tqdm_message = "Saving internal JS code ")

	def save_css_code(self , output_folder = os.getcwd() ,encoding = "utf-8"):
		''' Save CSS CODE into files 

		Parameters
		----------
		encoding:str
			The encoding to use during file read and write
		output_folder:str
			The folder where to save the CSS files   

		Returns
		-------
		None '''
		external_code_folder = os.path.join(output_folder ,"css/external")
		internal_code_folder = os.path.join(output_folder ,"css/internal")
		external_file_code_dict = {  os.path.join(external_code_folder , base_name):code for base_name,code in self.external_css_code.items()  }
		internal_file_code_dict = {  os.path.join(internal_code_folder , base_name):code for base_name,code in self.internal_css_code.items()  }
		self.save_static_code(external_file_code_dict , tqdm_message = "Saving external CSS code ")
		self.save_static_code(internal_file_code_dict, tqdm_message = "Saving internal CSS code ")

	def save_json_code(self , output_folder = os.getcwd() ,encoding = "utf-8"):
		''' Save CSS CODE into files 
		Parameters
		----------
		encoding:str
			The encoding to use during file read and write
		output_folder:str
			The folder where to save the JS files   

		Returns
		-------
		None '''
		internal_code_folder = os.path.join(output_folder ,"json/internal")
		internal_file_code_dict = {  os.path.join(internal_code_folder , base_name):code for base_name,code in self.internal_json_code.items()  }
		self.save_static_code(internal_file_code_dict, tqdm_message = "Saving internal JSON code ")

	


	def save(self  , output_folder:str = os.getcwd()  , download_images:bool = True , download_js:bool =True,
			download_css:bool = True , name_space:bool = True ) :
		'''Save a everything in ideal formats to a  specified outfolder 

			Structure example:

			---- Output folder/
					---- Report.txt
					---- Report.config
					---- Report.json
					---- page.html
					---- static/
							---- js/
							---- css/
							---- images/
							---- json 


		Parameters
		----------
		output_folder:str
			The folder where to save the JS files 
		download_images:bool
			Whether or not to download images
		download_js:bool
			Whether or not to download external Javascript static files  
		download_css:bool
			Whether or not to download external CSS static files  
		name_space:bool
			Whether or not to uniquely namespace the output folder using a time tag eg. OutputFolder_3rd_March/
		
		Returns
		-------
		None

		'''

		# reports
		if name_space:
			now = datetime.now()
			string_time = now.strftime("%H_%M_%A_%d_%Y")
			name = self.domain +"_WebpageReport_"+string_time
			output_folder = os.path.join(output_folder, name)
		check_folder(output_folder)
		json_report_file = os.path.join(output_folder , "Report.json")
		text_report_file = os.path.join(output_folder , "Report.txt")
		config_report_file = os.path.join(output_folder , "Report.config")
		html_file = os.path.join(output_folder , url_to_folder_name(self.url) + "_html_content.html")
		print("Writing report files ------------- " ,end ='')
		self.save_to_text_file(text_report_file)
		self.save_to_config_file(config_report_file)
		self.save_to_json_file(json_report_file)
		print("DONE!")
		print("Writing same site links info ----- " , end = '')
		with open(os.path.join(output_folder , "same_site_urls.txt") , 'w') as f:
			for l in self.same_site_urls:
				f.write(l + '\n')
		print("DONE")
		print("Writing other site links info ----- " , end = '')
		with open(os.path.join(output_folder , "other_site_urls.txt") , 'w') as f:
			for l in self.other_site_urls:
				f.write(l + '\n')
		print("DONE")
		#STATICS
		print("Loading static resources location  information  -----", end= "")
		if download_js:
			self.FetchExternalJS()
		if download_css:
			self.FetchExternalCSS()
		if download_images:
			self.FetchImages()
		print("External static code and resources fetched successfully .. ")
		print("saving static code ")
		self.save_js_code(output_folder = output_folder)
		self.save_css_code(output_folder = output_folder)
		self.save_images(output_folder = output_folder)
		self.save_json_code(output_folder = output_folder)
		print("Static code saved .")
		self.all_static_data.update(self.external_css_code )
		self.all_static_data.update( self.external_css_code )
		self.all_static_data.update( self.image_data)
		print("All static data parsed.")
		print("Writing HTML file ")
		with open(html_file , "w" , encoding = 'utf-8') as f:
			f.write(self.soup.prettify())
	


	def __repr__(self):
		# meta table
		metadata_table_list = [ [k,v] for k,v in self.metadata.items() ]
		metadata_table = tabulate(metadata_table_list)
		same_site_urls_number =len(self.same_site_urls)
		js_urls_number = len(self.js_urls)
		css_tags_number = len(self.css_tags)
		js_tags_number = len(self.js_tags)
		css_urls_number = len(self.css_urls)
		json_tags_number = len(self.json_tags)
		discovered_urls_number = len(self.discovered_urls)
		# urls stats
		urls_stats_table_list = [
			["Links from same site",same_site_urls_number] ,
			["Other site urls ", len(self.other_site_urls)],
			["Discovered links", discovered_urls_number],
			["Base url", self.base_url],
			["Network location", self.network_location],
		]
		url_stats_table = tabulate(urls_stats_table_list)
		# Static data 
		static_data_stats_table_list = [
			["External Javasript files", js_urls_number],
			['External CSS files' , css_urls_number],
			['Javascript  <script> tags',js_tags_number],
			["JSON tags " , json_tags_number],
			["CSS <style> tags" ,css_tags_number],
			["Image files", len(self.image_urls),], 
			["HTML tags processed" , self.elements_processed],
			]
		static_data_stats_table = tabulate(static_data_stats_table_list)
		repr_str = PAGE_REPORT_STRING.format(
			self.url,
				metadata_table,
				url_stats_table,
				static_data_stats_table)
		return repr_str
 

					 
	def __str__(self):
		return self.__repr__()