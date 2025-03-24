import requests , socket , os  ,time 
from bs4 import BeautifulSoup
from crawlfish.crawlfish_utils import check_file

 
def get_url(url:str,   session:requests.Session = None ,
			 params:dict = {} ,
			  headers:dict = {}  , 
			  retry_timeout:int = 5 , 
			  max_retries:int = 2000 , 
			  retry_count:int = 0 
			   ):
	''' Fetches a url and returns the response object 

	Parameters
	----------
	url:str
		The url to fetch 
	session:requests.Session
		The session class to use to fetch the url 
	headers:dict
		The GET headers
	params:dict 
		The GET parameters 
	retry_timeout:int 
		Time in seconds to wait in between retries 
	max_retries:int 
		The maximum number of retries allowed
	retry_count:int
		The current retry count 


	Returns
	-------
	response:requests.Response 
		A response instance obtained after fetching the url 

	'''
	if not session:
		session = requests.Session()

	print(f"Getting page ->  {url} " , end = '')
	try:
		response = session.get(url , params = params , headers = headers)
		print("DONE")
		return response
	except (requests.exceptions.ConnectionError , 
		requests.exceptions.ConnectTimeout, 
		requests.exceptions.ChunkedEncodingError,
		socket.gaierror, requests.exceptions.ReadTimeout
		 ):
		print("Connect error . Retrying ....\n ")
		if retry_count > max_retries:
			print("-------------------------MAX RETRY COUNTS ACHIEVED -----------------------------")
			raise
		retry_count += 1
		print("         \n            [RETRY {}]  \n".format(retry_count))
		time.sleep(retry_timeout)
		return get_url(url , session , params , headers , retry_timeout , max_retries , retry_count)
	except:
		raise



def get_page(url , session:requests.Session = None ,
			 params = {} ,
			  headers = {}  , 
			  retry_timeout = 5 , 
			  max_retries = 2000 , 
			  retry_count = 0 , 
			  output_file = "", 
			  soup = False ):
	'''
	This function fetches a url and returns the html of the web page
	If there is a problem with the connection it will retry as specified

	Parameters
	----------
	url:str
		The url to fetch 
	session:requests.Session
		The session class to use to fetch the url 
	headers:dict
		The GET headers
	params:dict 
		The GET parameters 
	retry_timeout:int 
		Time in seconds to wait in between retries 
	max_retries:int 
		The maximum number of retries allowed
	retry_count:int
		The current retry count 
	soup:bool
		Whether or not to return the data a BeautifulSoup instance 




	Returns
	-------
	bs4.BeautifulSoup object or the html string of the page fetched 
		 
	
	'''
	response =get_url(url , session )
	soup  = BeautifulSoup(response.content , 'html.parser')
	cont = soup.prettify() 
	if output_file:
		print("Writing response content to file {}".format(output_file) , end = '')
		check_file(output_file)
		with open(output_file , "w" , encoding = 'utf-8') as f:
			f.write(cont)
		print('DONE')
	
	if soup:
		return soup
	return cont 

	 

def get_page_with_driver(url , driver ,retry_timeout = 5 , 
			  max_retries = 20 , 
			  retry_count = 0 , 
			  output_file = "" ):
	'''Try to get a web page using a selenium.webdriver.WebDriver object 

	TO BE DONE ..too lazy lol 

	'''

	pass 