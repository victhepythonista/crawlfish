
from unittest import TestCase

from crawlfish.crawler import extract_file_info_from_url



class Test_extract_file_info_from_url(TestCase):

	def test_func(self):
		# basic scenario
		test_url = "http://www.site.com/video.mp4?jkdhflsdfhlgfbfdshbf"
		file , ext  = extract_file_info_from_url(test_url)
		self.assertTrue(file == "video.mp4")
		self.assertTrue(ext == '.mp4')
		# unclear extension scenario
		test_url = "http://www.site.com/file.min.js?jkdhflsdfhlgfbfdshbf"
		file , ext  = extract_file_info_from_url(test_url)
		print("FILE" , file , "ext" , ext)
		self.assertTrue(file == "file.min.js")
		self.assertTrue(ext == '.js')
		