from unittest import TestCase 

from crawlfish.crawler.get_url_parts import get_url_parts








class Test_get_url_parts(TestCase):

	def test_get_url_parts(self):
		test_url = "https://site.com/a/b/c/d"
		parts =  get_url_parts(test_url)
		print("PARTS " , parts)
		expected_outcome = [ 'https://site.com/a', 'https://site.com/a/b',
					'https://site.com/a/b/c' ]
		self.assertTrue(len(parts ) == 3)
		self.assertTrue(expected_outcome == parts)
