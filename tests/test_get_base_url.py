


from crawlfish.crawler.get_base_url import get_base_url

from unittest import TestCase 


class Test_explore_website(TestCase):

	def test_metadata(self):
		test_link = "https://stackoverflow.com/questions/"
		url = get_base_url(test_link)
		print("url " , url)
		self.assertTrue(url == 'https://stackoverflow.com' )

