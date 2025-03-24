import os
import urllib.parse 


def ensure_url_format(
	base_url:str ,
	url:str
	):
	''' Ensures that the url is full and starts with the base_url provided.... if not it will conjoin it with the base url

	Parameters
	----------
	base_url:str
		The base url eg . https://site.com
	url:str
		The url in question

	Returns
	-------
	str
		A url that meets requirements

	'''
	
	if url.startswith("http"):
		return url
	new_url =urllib.parse.urljoin(base_url , url)
	return new_url
