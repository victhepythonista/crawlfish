
import requests 
from crawlfish import explore_website ,explore_webpage , WebpageReport , WebsiteReport


webpage_url = "https://www.sample-videos.com/"

def custom_get_function(url):
	'''A custom fetch function to be used by crawlfish 
	It returns a requets.Response object'''
	print("Custom getting website")
	response = requests.get(url)
	print("Foun response")
	return response


# explore a website
website_report = explore_website(webpage_url , get_function = custom_get_function , crawl_limit = 2)


# explore a web page
webpage_report = explore_webpage(webpage_url , get_function = custom_get_function)


# Saving a webpage_report 
webpage_report.save(output_folder = "test_data/mypagereport/"  )
website_report.save(output_folder = "test_data/mysitereport/"  )

# You can also change the function any time and when you use
# the save()  method next time , it will fecth urls using the provided functions
webpage_report.get_function = custom_get_function
website_report.get_function = custom_get_function



