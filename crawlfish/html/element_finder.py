
import re , bs4 , os 
from bs4 import BeautifulSoup

from .get_element_text import get_element_text



def process_html_or_soup(html_or_soup):
	'''
	A little helper function that will try to return a BeautifulSoup object from a possible html string 

	'''
	default_soup = BeautifulSoup("" , "html.parser")
	soup = ""
	if type(html_or_soup ) == BeautifulSoup:
		return html_or_soup
	if not type(html_or_soup) == str:
		return default_soup
	# try to make a Beautiful Soup object
	soup = BeautifulSoup(html_or_soup , "html.parser")
	return soup



class ElementFinder:

	''' 
	This class is used to perform custom element searches within a html document represented as a BeautifulSoup object

	'''
	def __init__(self , html_or_soup ):
		self.soup = process_html_or_soup(html_or_soup)

	def find_elements(  self , 
						tag_name:str="" , tag_names:list=[] ,
						 attribute:str = "" , attributes:list = [] ,
						 attribute_value:str="" , attribute_values:list = [] , 
						  text_match:str= "" , text_matches:list = [] 
						    ):
		'''
		This function returns a list if elements that match all the provided specifications
		  and returns an empty list if none is found 

		Parameters
		----------
		tag_name:str
			name of the tag of interest 
		tag_names:list
		attribute:str
			Element attribute of interest
		attribute_value:str
			The attribute value to match , it can also be a regex
		text_match:str
			The text value to match in the elements , it can also be a regex 


		Returns
		-------
		elements:list 
			A list of elements that match the specified requirements 

		Raises
		------
	
		Scenarios:
		'''

		soup = self.soup # for shorter code , yeah, I'm that lazy
		tag_names = tag_names + [tag_name,]
		attributes = attributes + [attribute,]
		attribute_values = attribute_values + [ attribute_value ,]
		text_matches = text_matches + [text_match,]
		elements_that_match_tag_names = []
		elements_that_match_attributes = [] 
		elements_that_match_attribute_values = [] 
		elements_that_match_text_matches = []
		all_elements = soup.find_all()

		# collect elements_that_match_tag_names
		for tag_name in tag_names:
			elements = soup.find_all(tag_name)
			elements_that_match_tag_names += elements

		# collect elements_that_match_attributes
		for attribute in attributes:
			elements = []
			for element in all_elements:
				attrs = list(element.attrs.keys())
				# print("attributes for element ", element, attrs)
				if attribute in attrs:
					elements.append(element)
			elements_that_match_attributes += elements

		# collect elements_that_match_attribute_values
		for attribute_value in attribute_values:
			elements = []
			for element in all_elements:
				attr_values = list(dict(element.attrs).values())
				filtered_attr_values =  [] 
				for v in attr_values:
					if len(v) > 0 and  type(v) in (list ,bs4.element.AttributeValueList):
						for item in v:
							filtered_attr_values.append(item)
						continue
					items = v.strip().split()
					items = [  i.replace(" ", '') for i in items]
					for i in items:
						filtered_attr_values.append(i)
				attr_values = filtered_attr_values
				if attribute_value in attr_values:
					elements.append(element)
			elements_that_match_attribute_values += elements


		# collect elements_that_match_text_matches
		for text_match in text_matches:
			elements = [] 
			for element in all_elements:
				text = get_element_text(element)
				if re.search(text_match , text):
					elements.append(element)
			elements_that_match_text_matches += elements

		# Find the common elements and return them 
		all_collected_elements = elements_that_match_text_matches + elements_that_match_tag_names + elements_that_match_attributes + elements_that_match_attribute_values
		results = []
		register_check_map_list = lambda lst: True if not lst in ( [] , [''])  else False
		check_map_items = [ tag_names , attributes , attribute_values , text_matches]
		check_map =  list(map(  register_check_map_list , check_map_items ))  
		check_list = []
		if check_map[0]:
			check_list.append(elements_that_match_tag_names)
		if check_map[1]:
			check_list.append(elements_that_match_attributes)
		if check_map[2]:
			check_list.append(elements_that_match_attribute_values)
		if check_map[3]:
			check_list.append(elements_that_match_text_matches)
		for element in all_collected_elements:
			if element in results:
				continue
			check_result = [] 
			for check_list_item in check_list:
				sources = [el.__repr__() for el in check_list_item]
				check_result.append(element.__repr__() in sources)
			# print("check_result " , check_result)
			if all(check_result):
				results.append(element)
		return results
