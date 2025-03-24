
from unittest import TestCase

from crawlfish.html.get_first_attr_value import get_first_attr_value

from .test_soups import elements_to_find_soup



class Test_get_first_attr_value(TestCase):

	def test_finding_correct_values(self):

		soup = elements_to_find_soup
		# simple scenario
		value = get_first_attr_value(soup , "a" , "href")
		expected_value = "https://site.com"
		self.assertTrue(expected_value == value)
		

