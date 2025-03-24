
import re , bs4 , os 
from collections.abc import Iterable
from tqdm import tqdm 
from bs4 import BeautifulSoup
from bs4.element import AttributeValueList
from .get_element_text import get_element_text
from .ensure_soup import ensure_soup


class ElementFinder:

	''' 
	This class is used to perform custom element searches within a html string or BeautifulSoup object
	
	Parameters
	----------
	html_or_soup:[str,BeautifulSoup]
		The html info to search from
	'''
	def __init__(
		self ,
		html_or_soup:tuple[str,BeautifulSoup] 
		):
		self.soup = ensure_soup(html_or_soup)
		self.html = self.soup.prettify()

	def find_elements(  
		self , 
		tag_name:str="" ,
		tag_names:Iterable=[] ,
		attribute:str = "" ,
		attributes:Iterable = [] ,
		attribute_value:str="" ,
		attribute_values:Iterable = [] , 
		text_match:str= "" ,
		text_matches:Iterable = [] , 
		show_progress:bool = True ,
		num:int = 0
						    ):
		'''
		This function returns a list if elements that match all the provided specifications
		  and returns an empty list if none is found 

		Parameters
		----------
		tag_name:str
			tag name to match
		tag_names:Iterable
			Tag names to match 
		attribute:str
			Element attribute name to match
		attributes:Iterable
			A list of attribute names to match 
		attribute_value:str
			The attribute value to match , it can also be a regex
		attribute_values:Iterable
			A list attribute values to match , they can also be a regex
		text_match:str
			The text value to match  , it can also be a regex 
		text_matches:Iterable
			A list of text valies to match against element text values . They can also be regex
		show_progress:bool
			A flag to control verbosity, has not been inplemented yet , so no need using this now
		num:int
			The maximum number of elements to find . num = 0 returns all matched elements
		

		Returns
		-------
		elements:list 
			A list of elements that match the specified requirements 
			The items in the list are of type bs4.Tag

		'''
		print("Searching for elements ")
		soup = self.soup  
		tag_names = tag_names + [tag_name,]
		attributes = attributes + [attribute,]
		attribute_values = attribute_values + [ attribute_value ,]
		text_matches = text_matches + [text_match,]
		elements_that_match_tag_names = []
		elements_that_match_attributes = [] 
		elements_that_match_attribute_values = [] 
		elements_that_match_text_matches = []
		all_elements = soup.find_all()
		# # collect elements_that_match_tag_names
		# for tag_name in tag_names:
		# 	elements = soup.find_all(tag_name)
		# 	elements_that_match_tag_names += elements


		what_to_match = {
				"tag_name":True if ''.join(tag_names).strip() != '' else False  , 
				'attribute':True if ''.join(attributes).strip() != '' else False,
				'attribute_value':True if ''.join(attribute_values).strip() !=  '' else False,
				'text':True if ''.join(text_matches).strip() !=  '' else False,

		}
		matched_elements = [] 
		for element in tqdm(all_elements  , desc = "Finding elements "  ):
			if element in matched_elements:
				continue
			if not type(element) == bs4.Tag:
				continue
			tag_name_check = False 
			attribute_check = False
			attribute_value_check = False
			text_check  = False
			all_checks = []
			# check tag name 
			if what_to_match['tag_name']:
				if element.name in tag_names:
					tag_name_check = True
					all_checks.append(tag_name_check)
				else:
					all_checks.append(False)
			# check attribute 
			if what_to_match['attribute']:
				for attr in list(element.attrs.keys()):
					for attr_to_check in attributes:
						if attr == attr_to_check:
							attribute_check = True
							break 
				all_checks.append(attribute_check) 
							
			# check attriubte values
			if what_to_match['attribute_value']:
				for attr_value in list(element.attrs.values()):
					if type(attr_value) == AttributeValueList:
						if len(attr_value) > 0:
							attr_value = attr_value[0]
						else:
							continue
					if attr_value == '':
						continue
					for attr_value_to_check in attribute_values:
						if re.search(attr_value_to_check , attr_value ):
							attribute_value_check = True
							break
				all_checks.append(attribute_value_check)

			# check text matches
			if what_to_match['text']:
				for  text_to_match in text_matches:
					if text_to_match in (None , ''):
						continue
					element_text = get_element_text(element)
					if element_text.strip == "":
						continue
					if re.search(text_to_match , element_text):
						text_check = True 
						break 
				all_checks.append(text_check)

			# tag_name_check if what_to_match['tag_name'] else False,
			# attribute_check if what_to_match['attribute'] else False ,
			# attribute_value_check if what_to_match['attribute_value'] else False ,
			# text_check if what_to_match['text'] else False , ]
			# print("\n ~~ All checks for ", element , all_checks)
			if len(all_checks) == 0:
				continue
			if all(all_checks):
				matched_elements.append(element)
				if num > 0:
					if len(matched_elements ) == num:
						return matched_elements
		print("\n ============ SEARCH COMPLETE ! Found {} elements that match the search =========== \n ".format(len(matched_elements)))
		print(matched_elements)
		return matched_elements




 