import re , bs4
from bs4 import BeautifulSoup

from .element_finder import ElementFinder


def get_elements_text (html_or_soup ,tag_name:str="" , tag_names:list=[] ,
						 attribute:str = "" , attributes:list = [] ,
						 attribute_value:str="" , attribute_values:list = [] , 
						  text_match:str= "" , text_matches:list = []  ):
	'''
	Parameters
	-----------
	soup:BeautifulSoup
		The html soup with the elements of interest
	 
	Returns
	--------
	texts:list
		A list containing text data from the elements specified in the tag_info_list parameter
		Structure -> [ [ tag_name, attribute m attribute_value ] ..... ]
		'''
	elements = ElementFinder(soup).find_elements(tag_name, tag_names , attribute , 
												attributes , attribute_value , attribute_values , 
												text_match , text_matches )
	texts = [ get_element_text(element) for element in elements ]
	return texts
