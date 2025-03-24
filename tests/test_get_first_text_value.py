
from unittest import TestCase

from crawlfish.html.get_first_text_value import get_first_text_value

from .test_soups import elements_to_find_soup



class Test_get_first_text_value(TestCase):

	def test_finding_correct_values(self):

		soup = elements_to_find_soup
		# simple scenario
		value = get_first_text_value(soup , "a" )
		expected_value = "nolinkhere"
		self.assertTrue(expected_value == value)
		

