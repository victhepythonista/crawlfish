import re 


def get_base_url(url:str):
	''' Gets the main starting point of a website;s url .
	Eg . https//:site.com/page/data/hello 

		 will be :

		 https://site.com
	
	Parameters
	----------
	url:str
		The url to extract the base url from 

	Returns
	-------
	url:str
		The base url found
	'''
	# Look for the third slash 
	needed_charchters = '/' , 'http' , ':' 
	if not all([ char in url for char in needed_charchters  ]):
		print("Could not get base url : {}".format(url))
		return url
	if url.count('/') >= 3:
		occurrences = [ i.start()  for i in re.finditer('/', url)]
		end = occurrences[2] # the third / 
		return url[:end]
	return url