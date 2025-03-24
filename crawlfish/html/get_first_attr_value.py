import bs4 
from collections.abc import Iterable
from bs4 import BeautifulSoup
from .get_element_text import get_element_text
from .element_finder import ElementFinder

def get_first_attr_value( 
	html_or_soup:tuple[str,BeautifulSoup]   ,
	tag_name:str ,
	attribute:str ,
	tag_names:Iterable  = [],  
	attributes:Iterable = [] , 
	text_match:str = '' ,
	text_matches:Iterable = []   ):
	''' This functions returns the first non-empty attribute value from elements that match the search parameters 
	
	Parameters
	-----------
	html_or_soup:BeautifulSoup
		The html string or  soup to search from
	tag_name:str
			tag name to match
	tag_names:abc.Iterable
		Tag names to match 
	attribute:str
		Element attribute name to match
	attributes:list
			A list of attribute names to match 
	text_match:str
		The text value to match  , it can also be a regex 
	text_matches:list
		A list of text valies to match against element text values . They can also be regex
	 
	Returns
	-------
	value:str
		The first non-empty attribute value found 
	'''
	tag_names = tag_names + [tag_name,]
	attributes = attributes + [attribute,]
	text_matches = text_matches + [text_match,]
	finder = ElementFinder(html_or_soup)
	matching_elements  = finder.find_elements(tag_names = tag_names, attributes = attributes) + finder.find_elements(attributes = attributes,  text_matches = text_matches)
	for element in matching_elements:
		for attribute in attributes:
			value =element[attribute].strip() 
			if value  !='' :
				return value 

	return ''