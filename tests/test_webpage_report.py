import json
import os
from unittest import TestCase

from configparser import ConfigParser
from crawlfish.crawler.webpage_report import WebpageReport
from crawlfish import explore_webpage

from .test_soups import test_internal_static_soup

test_js_tags =  test_internal_static_soup.find_all("script")
test_css_tags =  test_internal_static_soup.find_all("style")

test_static_output_folder = 'tests/test_data/test_download_static_by_webpage_report/'

test_section_name , test_section_key = "urls", "network_location"
expected_network_location = "www.sample-videos.com"
test_url = "https://www.sample-videos.com/"

def test_get_url_function(url):

	return test_internal_static_soup


class TestWebpageReportClass(TestCase):

	def test_save_as(self):
		test_page_report = WebpageReport(test_url)
		dict_form = test_page_report.as_dict()
		self.assertTrue(type(dict_form) == dict )

		# config file
		test_file = "tests/test_data/page_report_config.ini"
		test_page_report.save_to_config_file(test_file)
		cp = ConfigParser()
		cp.read(test_file)
		self.assertTrue(len(cp.sections()) != 0)
		self.assertTrue(cp[test_section_name][test_section_key] == expected_network_location)

		# text file 
		test_file = "tests/test_data/page_report_text.txt"
		test_page_report.save_to_text_file(test_file)
		with open(test_file , "r") as f:
			self.assertTrue(f.read() == test_page_report.as_text())

		# json 
		test_file = "tests/test_data/page_report_json.json"
		test_page_report.save_to_json_file(test_file)
		with open(test_file ,"r") as f:
			data = json.load(f)
			dct = dict(data)
			self.assertTrue(dct[test_section_name][test_section_key] == expected_network_location)

	def test_extract_internal_code(self):
		''' '''
		test_page_report =   WebpageReport(test_url  , js_tags = test_js_tags , css_tags = test_css_tags)
		self.assertTrue("somescript1" in test_page_report.internal_js_code.values())
		self.assertTrue("somestyle2" in test_page_report.internal_css_code.values())

	def test_download_static_code(self):
		test_css_urls = ['https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css','https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.3.1/css/all.min.css']
		test_js_urls = ['https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js','https://unpkg.com/leaflet@1.9.4/dist/leaflet.js']
		test_page_report =   WebpageReport(test_url  , js_urls = test_js_urls , css_urls = test_css_urls, js_tags = test_js_tags , css_tags = test_css_tags)
		test_page_report.FetchExternalCode()
		test_page_report.save_js_code(output_folder = test_static_output_folder )
		test_page_report.save_css_code(output_folder = test_static_output_folder)

	def test_download_images(self):
		expected_output_file = os.path.join( test_static_output_folder + 'images' , "googlelogo_light_color_272x92dp.png",)
		if os.path.isfile(expected_output_file):
			os.remove(expected_output_file)
		test_image_urls = [ 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png',]
		test_page_report =   WebpageReport(test_url , image_urls = test_image_urls)
		test_page_report.FetchImages()
		test_page_report.save_images(test_static_output_folder)
		self.assertTrue(os.path.isfile(expected_output_file))
		
	def test_get_other_site_urls(self):
		test_page_report =   explore_webpage("https://site.com" , get_function = test_get_url_function)
		self.assertTrue("https://othersite.com" in test_page_report.other_site_urls)

	def test_save(self):
		test_page_report =   explore_webpage("https://amazon.com")
		print("STATIC URLS")
		print(test_page_report.js_urls)
		print(test_page_report.css_urls)
		test_page_report.save("tests/test_data/test_save_webpage_report" , name_space = True)
		print("URLS " , test_page_report.other_site_urls , test_page_report.same_site_urls)


 