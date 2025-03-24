import os 


from unittest import TestCase

from crawlfish.crawler import download_video , download_videos

test_video_link_1 = "https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4"
test_video_link_2 = "https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_5mb.mp4"

test_output_folder = "tests/test_data/test_video_download"

class TestDownloadVideo(TestCase):

	def test_download_video_function(self):
		# check if the file to be downloadd is found 
		expected_size = 2107842
		expected_path = os.path.join(test_output_folder , "big_buck_bunny_720p_2mb.mp4")
		if os.path.isfile(expected_path):
			os.remove(expected_path)
		file_name , data = download_video(test_video_link_1 , output_folder = test_output_folder)	
		print("FILE SIZE " , os.path.getsize(expected_path))
		self.assertTrue(os.path.isfile(expected_path))
		self.assertTrue(len(data) == expected_size)
		self.assertTrue(os.path.getsize(expected_path) == expected_size)


		# test providing custom file name 
		expected_path = os.path.join(test_output_folder , "myvideo.mp4")
		if os.path.isfile(expected_path):
			os.remove(expected_path)
		file_name , data = download_video(test_video_link_1 , output_folder = test_output_folder ,file_name = "myvideo")	
		self.assertTrue(os.path.isfile(expected_path))
		self.assertTrue(len(data) == expected_size)
		self.assertTrue(os.path.getsize(expected_path) == expected_size)

