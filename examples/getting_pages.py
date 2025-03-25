from crawlfish import get_page , get_url , get_page_with_driver

# get a requests.Response object of a page
response = get_page("https://www.sample-videos.com")

# get the html of a page
response = get_page("https://www.sample-videos.com")

# get the bs4.BeautifulSoup instance fo a page
soup = get_page("https://www.sample-videos.com" , soup = True )

# save the page to a file 
response = get_page("https://www.sample-videos.com" , output_file = "test_data/stack.html")

# Fetch a page with a  selenium webdriver
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
# Initialize your webdriver
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options = options)
html = get_page_with_driver( 'https://www.sample-videos.com' , driver)

# Fetch using a selenium webdriver and save a page to a file 
html = get_page_with_driver( 'https://www.sample-videos.com' , driver , output_file = "test_data/withdriver.html")


driver.quit()
