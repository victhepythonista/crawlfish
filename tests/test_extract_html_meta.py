from unittest import TestCase

from crawlfish.crawler.extract_html_meta import extract_html_meta

from .test_soups import test_extract_meta_soup


class TestExtractHtmlMEtafunc(TestCase):
	def test_func(self):
		test_soup = test_extract_meta_soup
		data = extract_html_meta(test_soup)
		print("Extracted test meta " , data)
		self.assertTrue('viewport' in data )
		self.assertTrue(data['viewport'] == '200x200')
