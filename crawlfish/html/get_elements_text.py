import re , bs4
from collections.abc import Iterable 
from bs4 import BeautifulSoup
from .element_finder import ElementFinder
from .get_element_text import get_element_text

def get_elements_text (
	html_or_soup:tuple[str,BeautifulSoup] ,
	tag_name:str="" ,
	tag_names:Iterable=[] ,
	attribute:str = "" ,
	attributes:Iterable = [] ,
	attribute_value:str="" ,
	attribute_values:Iterable = [] , 
	text_match:str= "" ,
	text_matches:Iterable = []  
						  ):
	'''Returns the texts in a list of all the elements that match the provided specs 

	Parameters
	-----------
	html_or_soup:BeautifulSoup
		The html string or  soup to search from
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
	 
	Returns
	--------
	texts:list
		A list containing text data from the elements specified 
		Format [ text1 , text2 ..... ]
		'''
	elements = ElementFinder(html_or_soup).find_elements(tag_name, tag_names , attribute , 
												attributes , attribute_value , attribute_values , 
												text_match , text_matches )
	texts = [ get_element_text(element) for element in elements ]
	return texts
