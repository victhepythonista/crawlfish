from urllib.parse import urlparse  # Python 3.x
from .get_base_url import get_base_url




def get_url_parts(url:str):
	'''This function splits a url and returns  possible routes of the url

	Example :
		Https://site.com/a/b/c/d

		to return 	[ https://site.com/a/ , https://site.com/a/b,https://site.com/a/b/c ]

	Parameters
	----------
	url:str
		The url to extract the possible url parts from

	Returns
	-------
	parts:list
		All possible url parts found
	'''
	path = urlparse(url).path[1:]
	base_url = get_base_url(url)
	parts = path.split('/')
	parts = [base_url+'/' + '/'.join(parts[:index+1]) for index in range(len(parts))]
	if url in parts:
		parts.pop(parts.index(url))
	return parts 

