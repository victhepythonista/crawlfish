

from crawlfish.crawler.explore_webpage import explore_webpage
from crawlfish import get_page
from unittest import TestCase 


def test_get_function(url):
	html = get_page(url , output_file = "tests/test_data/test_explore_webpage.html")
	return html
class Test_explore_webpage(TestCase):

	def test_page_report_returned(self):
		report = explore_webpage('https://amazon.com/' , test_get_function)
		# print(report.same_site_urls)
		expected_netloc = 'amazon.com'
		self.assertTrue(report.split_url.netloc == expected_netloc)