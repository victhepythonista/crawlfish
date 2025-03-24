import time
from tqdm import tqdm
from types import FunctionType
from crawlfish.http import get_url 
from .url_to_folder_name import url_to_folder_name
from .website_report import WebsiteReport
from .explore_webpage import explore_webpage
from .ensure_html_url import ensure_html_url

def explore_website(  
	url:str   ,
	get_function:FunctionType = get_url  ,
	crawl_limit:int = 0
	   ):
	''' Explores all links of a website stemming from the url provided. It will try to discover new parts of the website
	Parameters
	----------
	url:str
		The url to the website to be explored
	get_function:FunctionType
		A function for fetching the webpage ,
		it should take a url as its sole argument and return a html string or BeautifulSoup instance
	crawl_limit:int
		The maximum number of pages to be crawled

	Returns
	-------
	WebsiteReport
		A WebsiteReport instance containing all the scraped data 

	'''
	crawl_limit_check = True if crawl_limit != 0 else False 
	page_reports = {}
	url_pool = [url, ]
	fetched_urls = [  ] 
	discarded_urls = []
	current_url = url 
	count = 0 
	while url_pool != [] :

		print("=================== CRAWLING {} URL | CRAWL COUNUT =  {} | POOL SIZE = {} ==================".format(current_url, count , len(url_pool)))
		time.sleep(1)
		if crawl_limit_check:
			if count >= crawl_limit:
				print("Crawl limit reached ! ")
				time.sleep(1)
				break 
		if current_url in discarded_urls:
			if current_url in url_pool:
				url_pool.pop(url_pool.index(current_url))
			count += 1
			continue
		if not ensure_html_url(current_url ):
			if current_url in url_pool:
				url_pool.pop(url_pool.index(current_url))
			discarded_urls.append(current_url)
			count += 1
			continue
		if current_url in fetched_urls:
			count += 1
			if current_url in url_pool:
				url_pool.pop(url_pool.index(current_url))
				continue
			continue
		page_report = explore_webpage(current_url , get_function)
		folder_name = url_to_folder_name(current_url)
		page_reports[folder_name] = page_report
		fetched_urls.append(current_url)
		url_pool.pop(url_pool.index(current_url))
		urls = page_report.all_site_urls
		for u in urls :
			if u in fetched_urls:
				continue
			url_pool.append(u)
		url_pool = list(set(url_pool))
		for u in url_pool:
			if u in fetched_urls:
				url_pool.pop(url_pool.index(u))
		if len(url_pool) > 0:
			current_url = url_pool[0]
		count += 1
	report = WebsiteReport(page_reports)
	for pr in page_reports.values():
		print(pr)
	print("Discarded {} urls as they were not HTML page urls ".format(len(discarded_urls)))
	return report