from unittest import TestCase

from crawlfish import ElementFinder 

from .data import elements_to_find_soup


ef = ElementFinder(elements_to_find_soup)

class Test_FindingElements(TestCase):

	def test_finding_with_text_match(self):
		# We should get 3 elements that have the text 'randomperson' in them 
		elements = ef.find_elements(tag_name = "p" , text_match = "randomperson")
		self.assertTrue(len(elements) == 3 )
		elements = ef.find_elements(text_match = "randomperson")
		self.assertTrue(len(elements) == 5 ) # expeting 5 elements 


	def test_finding_by_attribute_value_only(self):
		# we expect 5 elements with an attribute value of 'ocean'
		elements  =ef.find_elements(attribute_value = "ocean")
		self.assertTrue(len(elements) == 5)

	def test_finding_by_tag_name_only(self):
		# expecting 3 <p> elements 
		elements = ef.find_elements(tag_name = "p")
		self.assertTrue(len(elements) == 3 )

	def test_finding_by_attribute_only(self):
		# we expect 6  elements with the 'class' attribute present  
		elements  =ef.find_elements(attribute = "class")
		self.assertTrue(len(elements) == 6)

	def test_finding_combos(self):
		elements = ef.find_elements(tag_name="h3"  ,  attribute_value = "heading")
		# expecting 2 elements 
		self.assertTrue(len(elements) == 2)
		# expecting 2 elements
		elements = ef.find_elements(text_match = "orbit" , attribute_value="planet")
		self.assertTrue(len(elements) == 2)
