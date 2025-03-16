import os , bs4
from bs4 import BeautifulSoup
from unittest import TestCase


from crawlfish.http import get_page 

test_link = "https://www.google.com/"
test_output_file  = "tests/test_get_google_page.html"




class TestHttpGet(TestCase):

	def test_get_page(self):
		'''
		Test if we can fetch a web page in an expected way 
		'''

		page = get_page(test_link)
		self.assertTrue(len(page) > 0)

	def test_get_and_save_page(self):
		'''
		Test if we can fetch a web page and save the contents in a file 
		'''
		if os.path.isfile(test_output_file):
	
		os.remove(test_output_file)
		page = get_page(test_link , output_file = test_output_file)
		self.assertTrue(len(page) > 0)
		self.assertTrue(os.path.isfile(test_output_file))
		with open(test_output_file , "r") as f:
			data = f.read() 
			soup = BeautifulSoup(data , "html.parser")
			self.assertTrue(len(data) > 0 ) # contains something 
			google_logo_image = soup.find("img" , {"alt":"Google"})
			self.assertTrue(type(google_logo_image) == bs4.Tag)

