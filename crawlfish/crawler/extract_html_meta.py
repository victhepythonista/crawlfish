from bs4 import BeautifulSoup

from crawlfish.html import ensure_soup , ElementFinder

def extract_html_meta(html_or_soup:tuple[BeautifulSoup,str]):
	''' This function extracts meta data information from a html page or bs4.BeautifulSoup  object and returns it in a dictionary

	Parameters
	----------
	html_or_soup:[str , BeautifulSoup]
		The html string or soup instance from where to extract the metadata from 
	
	Returns
	-------
	data:dict
		The metadata extracted in the format ->   { key:value..... }
	'''
	soup = ensure_soup(html_or_soup)
	finder = ElementFinder(soup)
	tags = soup.find_all("meta")
	data = {}
	attribute_combinations =[
			['name' ,'content'], 
			]
	for tag in tags:
		for combination in attribute_combinations:
			key_attr = combination[0]
			value_attr = combination[1]
			if tag.has_attr(key_attr) and tag.has_attr(value_attr):
				data[tag[key_attr]]=tag[value_attr]
	return data 
