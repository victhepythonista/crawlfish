import bs4 
from bs4 import BeautifulSoup 
from bs4.element import AttributeValueList


def get_first_with_attribute( soup:BeautifulSoup , tag_name:str , attribute:str , empty_attribute:bool = True  ):
	''' This function tries to return the  first matching element in a soup object that has the attribute present 


	Parameters
	----------
	soup:BeautifulSoup
		The BeautifulSoup instance containing the elements to be searched
	tag_name:str
		The tag name to match 
	empty_attribute:bool
		Whether or not the attribute being searched should contain a value . ie. It is not empty 

	Returns
	-------
	tag:bs4.Tag 
		The element found 
	None
		If no matching element is found
	'''


	tags = soup.find_all(tag_name)

	for tag in tags:
		if tag.has_attr(attribute):
			value =  tag.attrs[attribute ]
			if not  empty_attribute:
				if value.strip() != "":
					continue 
			return tag 

	return None 


	