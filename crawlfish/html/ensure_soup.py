import requests
from bs4 import BeautifulSoup

def ensure_soup(item:tuple[BeautifulSoup , requests.Response , str]):
	'''
	A little helper function that will try to return a BeautifulSoup object from the item provided
	return the item if its a soup

	Parameters
	----------
	item:[BeautifulSoup , requests.Response , str]
		The item to get a soup instance from 
	'''
	default_soup = BeautifulSoup("" , "html.parser")
	soup = ""
	if type(item ) == BeautifulSoup:
		return item
	if  type(item) == str:
		return BeautifulSoup(item , "html.parser")
	if type(item) == requests.Response:
		return BeautifulSoup(item.content , "html.parser")
	return default_soup
