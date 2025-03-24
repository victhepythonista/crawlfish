
from datetime import datetime

from crawlfish.crawler.explore_website import explore_website

from unittest import TestCase 

test_output_folder = "tests/test_data/test_explore_website_data"

test_link = 'https://www.countryle.com/'
'https://lakeviewequipment.com/'
'https://www.sample-videos.com'
"https://www.zetech.ac.ke/"

class Test_explore_website(TestCase):

	def test_func(self):
		wr = explore_website(test_link)
		wr.save(output_folder = test_output_folder)
		print("Here is the report")
		print(wr.page_reports.keys())

 