import os 
from unittest import TestCase

from crawlfish.crawlfish_utils import check_file



test_image_file = "tests/test_data/test_check_file/image.png"
test_text_file = "tests/test_data/test_check_file/some-file.txt"



class Test_check_file(TestCase):

	def test_func(self):
		if os.path.isfile(test_text_file):
			os.remove(test_text_file)
		check_file(test_text_file , make_if_none = False )
		self.assertFalse(os.path.isfile(test_text_file))
		check_file(test_text_file , make_if_none = True )
		self.assertTrue(os.path.isfile(test_text_file))
		