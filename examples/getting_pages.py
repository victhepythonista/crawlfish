from crawlfish import get_page , get_url 

# get a requests.Response object of a page
response = get_page("https://stackoverflow.com")

# get the html of a page
response = get_page("https://stackoverflow.com")

# get the bs4.BeautifulSoup instance fo a page
soup = get_page("https://stackoverflow.com" , soup = True )

# save the page to a file 
response = get_page("https://stackoverflow.com" , output_file = "test_data/stack.html")
