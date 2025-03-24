
import os 
from crawlfish.crawler import download_image ,download_images
from unittest import TestCase 

test_image_urls = ['https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg','https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg']
test_output_folder ="tests/test_data/test_download_images/"

class Test_download_image_function(TestCase):
	def test_download_image(self):
		test_file ="tests/google.png"
		test_link = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
		if os.path.isfile(test_file):
			os.remove(test_file)
		base_name , image_data = download_image( test_link , output_folder = test_output_folder)
		self.assertTrue(base_name == "googlelogo_light_color_272x92dp.png")


	def test_download_images(self):
		expected_path = os.path.join(test_output_folder , 'Sample-jpg-image-50kb.jpg')
		if os.path.isfile(expected_path):
			os.remove(expected_path)
		image_data = download_images(test_image_urls , output_folder = test_output_folder)
		self.assertTrue(os.path.isfile(expected_path))
		self.assertTrue('Sample-jpg-image-50kb.jpg' in image_data.keys())