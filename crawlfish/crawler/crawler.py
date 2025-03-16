
from tqdm import tqdm
from .save_option import SaveOption ,ExcelSaveOption , JsonSaveOption , JsonFileSaveOption, CSVSaveOption

default_save_option = CSVSaveOption("ScrapedData.csv")


class Crawler:

	'''This class is used to perform generic web a scraping fnctoins
	'''
	save_format = SaveFormat.EXCEL
	output_folder = os.getcwd()
	def __init__(self):
		empty_links = ""
		invalid_links = ""
		scraped_links = ""


	def scrape_links(self , links , scraping_function , scraping_function_args , scraping_function_kwargs , output_file = "scraped_data.csv" , save_option = default_save_option):
