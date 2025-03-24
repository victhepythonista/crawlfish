import json
from unittest import TestCase

from configparser import ConfigParser
from crawlfish.crawler.website_report import WebsiteReport
from crawlfish.crawler.url_to_folder_name import url_to_folder_name
from crawlfish.crawler import explore_webpage
from .test_soups import test_internal_static_soup

 

def test_get_url_function(url):

	return test_internal_static_soup



class TestwebsiteReportClass(TestCase):

	def test_save_fll_report(self):
		test_link = "https://supplypost.com"
		test_output_folder = "tests/test_data/test_save_web_report_function"
		page_reports ={ url_to_folder_name(test_link):explore_webpage(test_link  ) }
		report = WebsiteReport(page_reports)
		report.save(output_folder = test_output_folder , redownload_static = True)
		print(report.__repr__())