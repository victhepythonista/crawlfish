from unittest import TestCase 

from crawlfish.crawler.url_to_folder_name import url_to_folder_name



class Test_url_to_folder_name(TestCase):

	def test_get_url_parts(self):
		test_url = "https://site.uk/a/b/c/d"
		name =  url_to_folder_name(test_url)
		print("Test folder name generated " ,name)
		expected_outcome = "site__a_b_c_d"
		self.assertTrue(expected_outcome == name)

		test_url = "http://www.sample-videos.com/contact.php"
		name =  url_to_folder_name(test_url)
		print("Test folder name generated " ,name)
		expected_outcome = "sample_videos__contact_php"
		self.assertTrue(expected_outcome == name)