import os
import tldextract
from types import FunctionType
from urllib.parse import urlsplit, urlunsplit
from crawlfish.http import get_url
from crawlfish import ElementFinder , get_element_text
from .get_base_url import get_base_url
from .get_url_parts import get_url_parts
from .webpage_report import WebpageReport
from .website_report import WebsiteReport
from .ensure_url_format import ensure_url_format
from .extract_html_meta import extract_html_meta
from crawlfish.default_values import DATA_NOT_FOUND
from .ensure_html_url import ensure_html_url




def explore_webpage(  
	url:str  ,
	get_function:FunctionType = get_url
	 ):
	'''Crawls and goes through a webpage and returns a WebpageReport instance

	Parameters
	----------
	url:str
		The url of the webpage to be crawled
	get_function:FunctionType
		A function for fetching the webpage ,
		it should take a url as its sole argument and return a html string or BeautifulSoup instance

	Returns
	-------
	WebpageReport
		A WebpageReport instance containing all the juicy information
	'''
	print("\n\n=======================\n\n Exploring page ", url)
	html_or_soup = get_function(url)
	finder = ElementFinder(html_or_soup)
	soup = finder.soup
	base_url = get_base_url(url)
	tld_result = tldextract.extract(url)
	domain = tld_result.domain
	split_url = urlsplit(base_url) 
	print("Found base url " , base_url)
	print("Fetching elements --- " , end = '')
	all_elements = soup.find_all() 
	print("Done")
	# title 
	title_tag = soup.find("title")
	title = DATA_NOT_FOUND
	if not title_tag:
		title = DATA_NOT_FOUND
	else:
		title = get_element_text(title_tag)
	print("Page  <title> tag info fetched ")
	print("Extracting meta data ----- " ,end = '')
	metadata = extract_html_meta(soup)
	print("DONE")
	# Colleting images
	print("Collecting image links ---------------- ")
	image_tags = finder.find_elements(tag_name ="img" , attribute= "src")
	image_urls = [ensure_url_format( base_url , tag['src']) for tag in image_tags if tag["src"].strip() != '']

	print("DONE")
	# JAVASCRIPT DATA
	print("Collecting javascript data................" ,end = '')
	internal_js_tags = finder.find_elements( tag_name= "script"   )
	external_js_tags = finder.find_elements( tag_name= "script"  ,  attribute_value=".js" )
	# print("external_js_tags" , external_js_tags)
	js_files_urls = [ensure_url_format(base_url, tag["src"]) for tag in external_js_tags if tag.has_attr("src")]
	print("DONE")
	# CSS DATA
	print("Fetching CSS data.................." , end = '')
	external_css_tags = finder.find_elements(tag_name = "link" , attributes=["rel",'type'] , attribute_values=["stylesheet",'text/css'])
	css_files_urls = [ensure_url_format(base_url , tag["href"]) for tag in external_css_tags if tag.has_attr("href")]
	internal_css_tags = finder.find_elements(tag_name = "style" )
	print("DONE")
	# JSON DATA
	print("Fetching JSON.............." , end = '')
	json_tags = finder.find_elements(tag_name = 'script' ,attribute = "type" ,  attribute_value = 'application/json')
	print("DONE")
	# Remove JSON tags from inernal js tags
	print("Cleaning internal JS data..................." , end = '')
	json_text = [get_element_text(tag) for tag in json_tags]
	internal_js_tags = [tag for tag in internal_js_tags if not get_element_text(tag) in json_text]
	print("DONE")
	print("Collecting same site  urls ")
	href_tags = finder.find_elements(tag_name= 'a'  , attribute = 'href')
	possible_url_leads = []
	other_site_urls = [] 
	for tag in href_tags:
		print("URL poss", tag['href'])
		link = ensure_url_format(base_url , tag['href'])
		if not ensure_html_url(link):
			print("NOT TRUE URL ")
			continue
		tld_result = tldextract.extract(link)
		if tld_result.domain != domain:
			other_site_urls.append(link)
			continue
		if link in possible_url_leads:
			continue
		possible_url_leads.append(link)
	href_data =  [  tag["href"] for tag in href_tags if base_url in tag["href"] ]
	print("Checking links format")

	# generate the report 
	print("Generating report ---- " , end = '')
	page_report = WebpageReport(

			url = url , 
			title = title , 
			css_urls = css_files_urls , css_tags = internal_css_tags , 
			js_urls = js_files_urls , js_tags = internal_js_tags  , 
			json_tags = json_tags , image_urls = image_urls,
			same_site_urls = possible_url_leads , soup = soup,
			html = finder.html , other_site_urls = other_site_urls, 
			metadata= metadata
		)

	print("Page report generated !")
	print(page_report)
	return page_report




  