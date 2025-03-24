import bs4 
from collections.abc import Iterable 
from .get_element_text import get_element_text
from .element_finder import ElementFinder

def get_first_text_value( 
	html_or_soup:bs4.BeautifulSoup  ,
	tag_name:str ,
	attribute:str = '' ,
	tag_names:Iterable = [],  
	attributes:Iterable= [] , 
							    ):
	''' This functions returns the first non-empty text value from elements that match the search parameters 
	
	Parameters
	-----------
	html_or_soup:BeautifulSoup
		The html string or  soup to search from
	tag_name:str
			tag name to match
	tag_names:list
		Tag names to match 
	attribute:str
		Element attribute name to match
	attributes:list
			A list of attribute names to match 
	 
	Returns
	-------
	value:str
		The first non-empty text value found 
	empty_string:str
		An empty string if nothing is found 
	'''
	tag_names = tag_names + [tag_name,]
	attributes = attributes + [attribute,]
	finder = ElementFinder(html_or_soup)
	matching_elements  = finder.find_elements(tag_names = tag_names, attributes = attributes) 
	for element in matching_elements:
		value = get_element_text(element).strip()
		if value  !='' :
			return value 
	empty_string = ''
	return empty_string