

'''

This module contains functions for gettting an element from html or bs4 Soup


'''
import re , bs4
from bs4 import BeautifulSoup


def get_element_text(element:bs4.Tag , value_if_none = ""):
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


