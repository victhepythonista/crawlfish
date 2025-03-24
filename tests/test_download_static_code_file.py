
import os 
from crawlfish.crawler import download_static_code_file
from unittest import TestCase 


class Test_download_static_code_file_function(TestCase):
	def test_download_static_code_file(self):
		test_file ="tests/test_data/JQUERY_js.js"
		if os.path.isfile(test_file):
			os.remove(test_file)
		test_link = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"
		expected_content = '''e=this.originalEvent;this.isDefaultPrevented=Ne,e&&!this.isSimulated&&e.preventDefault()}'''
		base_name , code  = download_static_code_file( test_link	 ,file= test_file )
		print("base_name extracts" , base_name)
		self.assertTrue(base_name == 'JQUERY_js.js')
		self.assertTrue(expected_content in  code)
		with open(test_file  , "r" ,encoding = "utf-8") as f:
			self.assertTrue(expected_content in f.read())


		# test a lnik with arguments
		test_link = 'https://www.google.com/recaptcha/api.js?render=explicit'
		base_name , code = download_static_code_file(test_link)
		self.assertTrue(base_name == 'api.js')
		