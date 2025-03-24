from unittest import TestCase 

from crawlfish.crawler import ensure_html_url







class Test_gensure_is_html_url(TestCase):

	def test_func(self):
		test_url = "https://site.com/a/b/c/d.png?r=45,dfjd=er"
		result =  ensure_html_url(test_url)
		self.assertFalse(result)
