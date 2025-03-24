
from unittest import TestCase

from crawlfish.crawler.ensure_url_format  import ensure_url_format

from .test_soups import elements_to_find_soup



class Test_ensureurlformat_function(TestCase):
	def test_func(self):
		base_url = "https://site.com" 
		test_link = '/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js'
		expected_result = base_url  + test_link
		res = ensure_url_format(base_url, test_link)
		print('RESULT' , res)
		self.assertTrue(res == expected_result)