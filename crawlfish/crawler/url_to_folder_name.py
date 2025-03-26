import tldextract
from urllib.parse import urlparse   
from string import ascii_uppercase, digits ,ascii_lowercase , printable 


def clean_split_part(part:str):
	'''Remove unwanted url charchters from a url part 

	Parameters
	----------
	part:str
		The part of the url to clean

	Returns
	-------
	result:str
		A string that meets all the requirements 

		 '''
	wanted_charachters = ascii_lowercase + ascii_uppercase + digits  + '_'
	part = part.replace('-', '_')
	result = ''
	for char in part:
		if char in wanted_charachters:
			result += char
	return result


	
def url_to_folder_name(url:str):
	"""Converts a url to a value that can be used as a folder name safely

	Parameters
	----------
	url:str
		The url to get a folder name from 

	Returns
	-------
	folder_name:str
		A folder name that works (is valid or won't raise an error)"""
	# get base url first
	result = tldextract.extract(url)
	domain = result.domain
	path = urlparse(url).path.replace('.', '_')
	split = path.split('/')
	path = "".join(['_'+ clean_split_part(item) for item in split ])
	folder_name = clean_split_part( domain  + path)

	return folder_name
