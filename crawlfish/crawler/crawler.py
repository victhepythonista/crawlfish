
from tqdm import tqdm

from .save import ListDataSaver
from .save_option import SaveOption ,ExcelSaveOption , JsonSaveOption , JsonFileSaveOption, CSVSaveOption

default_save_option = CSVSaveOption("ScrapedData.csv")


class Crawler:

	'''This class is used to perform generic web a scraping fnctoins
	'''
	save_format = SaveFormat.EXCEL
	output_folder = os.getcwd()
	def __init__(self):
		self.save_option = CSVSaveOption




	def scrape_links(self , urls , scraping_function , scraping_function_args , 
						scraping_function_kwargs , output_file = "scraped_data.csv" ,
						 save_option = self.save_option):
		'''

		Returns
		--------
		scraped_data 

		'''
		scraped_data = []
		for url in tqdm(urls):
			data = scraping_function(*scraping_function_args , **scraping_function_kwargs)
			scraped_data.append(data)
		data_saver = ListDataSaver()
		data_saver.save_by_option(scraped_data , save_option)


