import requests , socket , os


def get_page(url , session:requests.Session = None ,
			 params = {} ,
			  headers = {}  , 
			  retry_timeout = 5 , 
			  max_retries = 20 , 
			  retry_count = 0 , 
			  output_file = ""):
	'''
	This function gets the html of a web page
	If there is a problem with the connection it will retry as specified

	Parameters
	-----------
	url:str
		The url to the web page you want to fetch 
	session:requests.Session
		A session object
	params:dict 
	headers:dict
	
	'''

	if not session:
		session = requests.Session()

	print(f"Getting page ->  {url} ")
	try:
		res = session.get(url , params = params , headers = headers)
		cont = str(res.content)
		if output_file:
			if not os.path.isfile:
				try:
					folder ,file = os.path.split(output_file)
					if not os.path.isdir(folder):
						os.makedirs(folder)
					with open(output_file , "w" ) as f:
						f.write("")
				except :
					raise
			with open(output_file , "w") as f:
				f.write(cont)
		return cont
	except (requests.exceptions.ConnectionError , 
		requests.exceptions.ConnectTimeout, 
		requests.exceptions.ChunkedEncodingError,
		socket.gaierror, requests.exceptions.ReadTimeout
		 ):
		print("Connect error . Retrying ....\n ")
		print("         \n            [RETRY {}]".format(retry_count))
		retry_count += 1
		return get_page(url , session , params , headers , retry_timeout , max_retries , retry_count)
	except:
		raise