import re , bs4
from bs4 import BeautifulSoup


def get_element_text(element:bs4.Tag , value_if_none:bool = ""):
	''' Get the text value of an element 

	Parameters
	----------
	element:bs4.Tag
		The element to extract text from 
	value_if_none:str
		What to return if text is not found 

	Returns
	str
		The text value found or value_if_none'''
	if element is None :
		return value_if_none
	else:
		st = element.string 
		if st:
			return st 
		tx = element.text 
		if tx:
			return tx 
	return value_if_none


