import os
import csv
from unittest import TestCase 

from crawlfish.crawlfish_utils import check_file
from crawlfish.crawler.crawler import UrlsCrawler 
from crawlfish import CSVSaveOption


 

TEST_WEBPAGE_DATA_DICT = {
	"https://company_website1.com":["company_website1" , "CEO1"],
	"https://company_website2.com":["company_website2" , "CEO2"],
	"https://company_website3.com":["company_website3" , "CEO3"],
	"https://company_website4.com":["company_website4" , "CEO4"],

} 
TEST_URLS = list(TEST_WEBPAGE_DATA_DICT.keys())

TEST_WEBPAGE_DATA_LIST = list(TEST_WEBPAGE_DATA_DICT.values())
WEBPAGE_DATA_HEADERS = ["COMPANY_NAME" , "CEO_NAME"]

test_csv_output_file ="tests/test_data/test_scraped_data.csv" 
test_csv_save_option = CSVSaveOption(test_csv_output_file)
def test_scrape_url(*args , **kwargs):
	# print("Scraping link " )
	# print(args  , kwargs)
	return TEST_WEBPAGE_DATA_DICT[args[0]]


class Test_UrlsCrawler(TestCase):

	def test_simple_Scraping_Scenario(self):
		crawler = UrlsCrawler( )
		if os.path.isfile(test_csv_output_file):
			os.remove(test_csv_output_file)
		crawler.save_option = test_csv_save_option
		data = crawler.scrape_urls(
			TEST_URLS , test_scrape_url , WEBPAGE_DATA_HEADERS , 
			    ) 
		self.assertTrue(data == TEST_WEBPAGE_DATA_LIST)
		# CHECK IF DATA IS WRITTEN OK 
		with open(crawler.save_option.file, "r") as f:
			reader = csv.reader(f)
			rows = [[i for i in row] for row in reader]
			self.assertTrue(rows[1:] == TEST_WEBPAGE_DATA_LIST )



