import os
from types import FunctionType
from collections.abc import Iterable
from tqdm import tqdm
from crawlfish.crawlfish_utils import check_file
from .save import ListDataSaver
from .save_options import save_formats, SaveOption ,ExcelSaveOption  
from .save_options import  JSONSaveOption , JSONFileSaveOption, CSVSaveOption 

default_csv_save_option = CSVSaveOption("ScrapedData.csv")

def check_save_option(save_option , crawler_object):
	''' Checks if a saveoption instance is supported , raises an Error of not'''
	supported = crawler_object.supported_save_option_instances
	if not save_option in supported:
		raise UnsupportedSaveOptionInstanceError(save_option , supported)

class Crawler:
	'''This is the base class for crawling
	'''
	supported_save_option_instances = CSVSaveOption , JSONSaveOption , JSONFileSaveOption , ExcelSaveOption
	output_folder = os.getcwd()
	def __init__(self , save_option = default_csv_save_option):
		self.save_option = save_option

	  

class UrlsCrawler(Crawler):
	''' This Crawler is used as a wrapper for  scraping  a list of urls using a function that takes the url as a parameter and returns data from one url'''

	def __init__(self , save_option:SaveOption = default_csv_save_option ):
		Crawler.__init__(self , save_option)



	def scrape_urls_in_file(
		self ,
		file:str ,
		scrape_function:FunctionType ,
		data_headers:Iterable ,  
						 save_option:SaveOption = None ):
		'''This method scrapes urls that are found in the text based file provided

		Parameters
		----------
		file:str
			The name of the file containing the urls 
		scraper_function:FunctionType
			A function that takes a url as it's sole parameter and returns a list of items scraped from the website . 
		data_headers:Iterable
			The headers for the data to be scraped eg. [NAME , AGE , SUBJECT ....]
			The number of items should be the same length as the list returned by the scrape_function
		save_option:SaveOption
			A SaveOption instance that specifies how the data should be saved 

		Returns
		-------
		scraped_data:list
			A list of the data scraped in this format : [  data_headers , [ row1_column1 , row1_colum2 ] , [ row2_column1 , row2_column2 ].....]
		'''
		
		if not save_option:
			save_option = self.save_option
		if not check_file(file):
			raise FileNotFoundError("Could not find the file [{}]".format(file))
		urls = [] 
		with open(file , 'r') as f:
			urls = f.readlines()
		return self.scrape_urls(urls , scrape_function , 
								data_headers, save_option  )

		
	def scrape_urls(self , urls:tuple[list , tuple ,set , iter ] , scrape_function:FunctionType , data_headers:tuple[list, tuple , set, iter],  
					 
						 save_option:SaveOption = None ):
		'''Scrapes a list of urls using the scrape function provided and returns the data 
		Parameters
		----------
		urls:[list,tuple ,set , iter ]
			The iterable containing the urls you want to scrape 
		scraper_function:FunctionType
			A function that takes a url as it's sole parameter and returns a list of items scraped from the website . 
		data_headers:Iterable
			The headers for the data to be scraped eg. [NAME , AGE , SUBJECT ....]
			The number of items should be the same length as the list returned by the scrape_function
		save_option:SaveOption
			A SaveOption instance that specifies how the data should be saved 	

		Returns
		-------
		scraped_data:list
			A list of the data scraped in this format : [  data_headers , [ row1_column1 , row1_colum2 ] , [ row2_column1 , row2_column2 ].....]
		

		'''
		if not save_option:
			save_option = self.save_option
		scraped_data = []
		for url in tqdm(urls):
			data = scrape_function(url)
			scraped_data.append(data)
		# add headers to the data 
		scraped_data_to_write = [data_headers, ] + scraped_data
		data_saver = ListDataSaver()
		data_saver.save_by_option(scraped_data_to_write , save_option)
		return scraped_data

 
 
 