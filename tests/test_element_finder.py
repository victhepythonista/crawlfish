from unittest import TestCase

from crawlfish import ElementFinder 

from .test_soups import elements_to_find_soup


ef = ElementFinder(elements_to_find_soup)

class Test_FindingElements(TestCase):

	def test_finding_with_text_match(self):
		# We should get 3 elements that have the text 'randomperson' in them 
		elements = ef.find_elements(tag_name = "p" , text_match = "randomperson")
		self.assertTrue(len(elements) == 3 )
		print(elements)
		elements = ef.find_elements(text_match = "randomperson")
		self.assertTrue(len(elements) == 5 ) # expeting 5 elements 


	def test_finding_by_attribute_value_only(self):
		# we expect 5 elements with an attribute value of 'ocean'
		elements  =ef.find_elements(attribute_value = "ocean")
		self.assertTrue(len(elements) == 6)

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
		# expecting 2 <h3> elements 
		self.assertTrue(len(elements) == 2)
		# expecting 2 elements
		elements = ef.find_elements(text_match = "orbit" , attribute_value="planet")
		self.assertTrue(len(elements) == 2)

	def test_finding_with_num_kwarg(self):
		elements = ef.find_elements(tag_name="a" , num =1 )
		# expecting 1 <a> elements 
		self.assertTrue(len(elements) == 1)

	def test_finding_with_attr_value_attr_tag_name(self):
		elements = ef.find_elements(tag_name="div" ,attribute = "id" , attribute_value = "name")
		# expecting   2 elements 
		self.assertTrue(len(elements) == 2)

	def test_complex_combo(self):
		html = """
		<!DOCTYPE html>
		<html>
		<head>
			<title> Let's find elements </title>
		</head>
		<body>

		<div id="person" class="person-container" > 
			 Someone had an email and it was someemail@gmail.com , yeah , his name was Ail Someem
		</div>

		<div id="" class="" ></div>
		<div id="" class="" ></div>
		<div id="" class="" ></div>

		<div id="" class="email-div" ></div>

		<p id="email-p" >validemail@gmail.com</p>
		<p id="email-p" ></p>
		<p id="" class="email-p"></p>
		<p id="" class="email-p"></p>
		<div id="" class="email-div" >Anothervalidemail@gmail.com</div>
		<div id="" class="email-div" ></div>

		<p id="" class="email-p"></p>

		<a id="" class="" ></a>
		<a id="" class="" ></a>
		<a id="" class="" ></a>
		<a id="" class="" ></a>
		<a id="" class="" ></a>



		</body>
	</html>

		"""
		email_regex = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+" 
		finder = ElementFinder(html)
		elements = finder.find_elements(  attributes = [ "id" , "class"] , attribute_values = ['email' , ] ,
			 tag_names = [ 'div' , 'p'] ,text_matches = [email_regex, ]    )
		expected_number_of_elements = 3
		self.assertTrue(len(elements) == expected_number_of_elements)