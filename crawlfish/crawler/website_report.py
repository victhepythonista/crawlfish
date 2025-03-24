import os
from collections.abc import Iterable
from datetime import datetime
from tabulate import tabulate
from tqdm import tqdm
from .url_to_folder_name import url_to_folder_name


SUMMARY_REPORT = """

Crawlfish has successfully scraped all {} links 

I'm working on this summary (I'm lazy) so more is to come in the next versions ....................

"""

class WebsiteReport:
	''' This class is to be used as a contaoiner for all the data collected during website crawling 

	Parameters
	----------
	page_reports:dict
		A dictionary containing page reports. Format -> { folder_name:WebpageReport }
	'''

	def __init__(self , page_reports:dict):
		self.page_reports = page_reports
		self.js_files_num =0 
		self.css_files_num = 0 
		self.images_num = 0 
		self.other_site_urls = []
		self.elements_processed = 0
		self.process_stats()

	def __repr__(self):
		text = "{}".format(tabulate( [
				["Pages crawled" ,len(self.page_reports.keys())],
				["Other site urls found", len(self.other_site_urls)],
				["CSS files found" , self.css_files_num] , 
				["Javascript files found" , self.js_files_num],
				["Image files found", self.images_num],
				["HTML tags processed" ,self.elements_processed],
				]
				))
		return text 
	def __str__(self):
		return self.__repr__()


	def process_stats(self):
		''' Prepare and compute necessary stats and class attributes '''
		for pr in self.page_reports.values():
			self.images_num += len(pr.image_urls)
			self.js_files_num += len(pr.js_urls)
			self.css_files_num += len(pr.css_urls)
			self.other_site_urls += pr.other_site_urls
			self.elements_processed += pr.elements_processed

	def  save(self  , output_folder = os.getcwd()  , download_images:bool = True ,
				 download_js:bool =True , download_css:bool= True , redownload_static:bool=False , 
				 exclude_static:Iterable = [] , name_space:bool = True ):
		''' Save the website information obtained by saving the web report classes and saving general website information 

		Parameters
		----------
		output_folder:str
			The folder where to save the data 
		download_images:bool
			Whether or not to download images
		download_js:bool
			Whether or not to download external Javascript static files  
		download_css:bool
			Whether or not to download external CSS static files  
		name_space:bool
			Whether or not to uniquely namespace the output folder using a time tag eg. OutputFolder_3rd_March/
		redownload_static:bool
			Whether or not to redownload static files that have already been downloaded instead of caching the data
		exclude_static:Iterable 
			A list of static file types to NOT download 
		name_space:bool 
			Whether or not to name space the page report save folders 


		Returns
		-------
		None
		'''
		now = datetime.now()
		static_urls_processed = [] 
		static_data_downloaded = {}
		string_time = now.strftime("%H_%M_%A_%d_%Y")
		output_folder  = os.path.join(output_folder , "Website_report_"+  string_time)
		site_report_file = os.path.join(output_folder , "Site Report.txt")
		other_site_urls_file =os.path.join(output_folder , "Other site urls.txt")
		summary_report_file =os.path.join(output_folder , "Summary.txt")

		for folder_name , page_report in tqdm(self.page_reports.items(), "Saving page report --- "):
			page_report_folder = os.path.join(output_folder,folder_name)
			if redownload_static:
				page_report.already_downloaded_static = static_data_downloaded
			download_images  ,download_js , download_css = False if 'img' in exclude_static else True  , False if 'js' in exclude_static else True  , False if 'css' in exclude_static else True  

			page_report.save(output_folder = page_report_folder , download_images = download_images , download_js = download_js , download_css= download_css , name_space = name_space)
			static_data_downloaded.update(page_report.all_static_data)



		with open(site_report_file , "w") as f:
			f.write(self.__repr__())

	 