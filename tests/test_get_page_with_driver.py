import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from crawlfish import get_page_with_driver


options = Options()
options.add_argument("--headless")
print("Creating a Firefox driver for testing ..........." , end = '')
test_driver = webdriver.Firefox( options = options)
print("DONE !")
test_url = "https://www.sample-videos.com/"
test_output_file = "test_data/Test_get_page_with_webdriver/samplevides.html"


class Test_get_page_with_webdriver(TestCase):

	def test_Raises_driver_type_error(self):
		with self.assertRaises(ValueError):
			get_page_with_driver(test_url , 'driver')

	def test_get_html(self):	
		page = get_page_with_driver(test_url , test_driver)
		self.assertTrue(page.strip() != '')

	def test_save_to_file(self):
		if os.path.isfile(test_output_file):
			os.remove(test_output_file)
		page = get_page_with_driver(test_url , test_driver , output_file = test_output_file)
		self.assertTrue(os.path.isfile(test_output_file))
		with open(test_output_file , "r") as f :
			data = f.read()
			self.assertTrue(len(data) > 0)