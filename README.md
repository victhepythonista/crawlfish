<p align="center" >
CRAWLFISH
</p>                                  


<div align="center">

  <img src="https://i.ibb.co/YTTFtDb9/crawlfish-purple-Untitled.png" alt="Logo" height="300"/> 
</div>



<div align="center">
<a href="https://www.python.org/"><img height=30  src="https://img.shields.io/badge/built%20with-Python3-blue.svg" alt="built with Python3"></a>

<a href="https://pepy.tech/projects/crawlfish"><img  height=30 src="https://static.pepy.tech/badge/crawlfish" alt="PyPI Downloads"></a>
		 
<a href="https://github.com/victhepythonista/crawlfish"><img height=30   src="https://img.shields.io/github/stars/victhepythonista/crawlfish.svg?style=social&label=Stars"></a>
</div>


---


- An easy to use web crawling Python package packed with handy functions for exploring whole websites or single webpages , dynamic element searching , generic web scraping  and  more . It also has helpful shortcut functions for bs4 , requests and selenium .
- It is simple and easy to understand
- You can use it in Python (.py) files or directly from the **command line**
- For more documentation go to the **docstrings** . I am yet to publish the full documentation , TBA.
- Read <a href="https://github.com/victhepythonista/crawlfish/blob/main/CONTRIBUTING.md" target="_blank">this</a> if you want to contribute and <a href="https://github.com/victhepythonista/crawlfish/blob/main/RELEASE_NOTES.md" target="_blank">here</a> to read the latest release notes .
- Ensure to install VERSION 0.0.8 and above 

 #### Key classes :

- <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/webpage_report.py" target="_blank">WebpageReport </a>
   Contains information collected after exploring a webpage
- <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/html/element_finder.py" target="_blank">ElementFinder</a>
	-A handy class that allows you to flexibly search for elements in a bs4.BeautifulSoup instance or a HTML string . 
	 Has **regex** support when searching for text matches and atribute values  
-  <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/website_report.py" target="_blank">WebsiteReport </a>
		Contains information collected after exploring a website
-  <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/crawler.py" target="_blank">UrlsCrawler</a>
	For generic web scraping programs that scrap urls from a list or file containing the urls line by line 
-  <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/save.py" target="_blank">ListDataSaver</a>
	Used to save data in a list into different forms ie .xlsx , .csv , .JSON . 
	 Created to fill the need of having to create/copy a saving function every time you make a new web scraper . The catch is that the data should be in a specific format -> **format [ [ header1,header2 ] , [ data1 , data2 ],......... ]**
-  <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/save_options.py" target="_blank">SaveOption </a>

#### Key functions :
-  <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/http/get.py" target="_blank">get_page() </a>
	Fetches a url , returns either a bs4.BeautifulSoup instance or a requests.Response instance  
		You can also save the HTML output to a file
- <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/explore_website.py" target="_blank">explore website() </a>
	Aggressively goes through a website one url at a time grabbing all needed data along the way . It will scrape the website until every url of the website has been processed .
		Returns a crawlfish.WebsiteReport object that contains all the juicy information

- <a href="https://github.com/victhepythonista/crawlfish/blob/main/crawlfish/crawler/explore_webpage.py" target="_blank">explore_webpage() </a>
	Collects static code , static files urls , metadata , urls of the same site and other info from a web page . 
		Returns a WebpageReport object that contains the information scraped
	



 
---



## Installation

- Install via pip 

```
pip install crawlfish
```
### Dependencies

- bs4
- tldextract
- tabulate
- tqdm
- requests
- selenium
- openpyxl




---


# Command line usage

- Here is a quick intro on how to use this library on the cmd

- The command below will crawl the Stackoverflow website up to a depth of 5 webpages starting from the url provided and save the data in the current directory  


```
python -m crawlfish --crawl-site --url https://stackoverflow.com --crawl-limit 5
```

- You can add urls on the command line or provide a text based file containing the urls 

- See all available commands by typing :


```
python -m crawlfish -h
```

- The help output looks like this:

```
  ___  ___    __    _   _   _     ___   _    __   _  _
 / _/ | _ \  /  \  | | | | | |   | __| | | /' _/ | || |
| \__ | v / | /\ | | 'V' | | |_  | _|  | | `._`. | >< |
 \__/ |_|_\ |_||_| !_/ \_! |___| |_|   |_| |___/ |_||_|



by Victor Kipkemboi | scriptilapia@gmail.com

====================================================================================================================

usage: __main__.py [-h] [-d | -cp | -cs] [-rs] [-u [URL ...]] [-uf URLS_FILE] [-i | -v | -tf] [-es [{js,css,img} ...]] [-f FILE | -fn FILE_NAME |
                   -outd OUTPUT_DIR] [-cl CRAWL_LIMIT]

options:
  -h, --help            show this help message and exit
  -d, --download        Download a file or files
  -cp, --crawl-page     Crawl a webpage or webpages
  -cs, --crawl-site     Crawl a website or websites
  -rs, --redownload-static
                        This option present means that static files with similar urls from different web pages will be downloaded evertime they are
                        found instead of caching the data since they are most likely similar.
  -u, --url [URL ...]   The URL(s) you want to process . Make sure to add spaces in between the urls
  -uf, --urls-file URLS_FILE
                        The path or name of a file containing urls to be processed
  -i, --image           Indicate that you are downloading an image. Eg: .png , .jpeg , .jpg
  -v, --video           Indicate that you are downloading a video. Eg: .mp4 , .mp3 , .mkv ....
  -tf, --text-file      Indicate that you are downloading a text-based file . Eg: .js, .txt , .css
  -es, --exclude-static [{js,css,img} ...]
                        Static file to not download during crawling processes . This option will have no effect during downloading
  -f, --file FILE       The name to be given to the FILE you want to download. Has no effect when many url(s) are downloaded . Make sure to include
                        the correct extension for convenience
  -fn, --file-name FILE_NAME
                        The name you want to give to the downloaded file . The extension will be added automatically . To be used only when one url
                        has been provided otherwise it has no effect whatsoever
  -outd, --output-dir OUTPUT_DIR
                        The directory where you want your output stored . The current directory will be used if none is provided . If the process
                        has no use for this , it will have no effect
  -cl, --crawl-limit CRAWL_LIMIT
                        The number of maximum urls to crawl when crawling a website or a webpage . 0 = Infinity , the default is 0 . This option
                        takes effect during site crawling only

(coon_venv) C:\Users\USER\Documents\GitHub\crawlfish>



```



---

# QUICK START

- A brief straightfoward tutorial of the library's main functions and  key classes .
- Let's get started with some examples !




---


### Crawling a web page

- A quick example of crawling the Stackoverflow landing web page


```python
>>> from crawlfish import explore_webpage , explore_website 
>>> # Lets expore a web page 
>>> page_report = explore_webpage("https://stackoverflow.com")
>>> # returns a crawlfish.WebpageReport object 

>>> # Save the scraped data 
>>> page_report.save( output_folder = "mydata" )
>>> # a folder named my data will be created and youll find all the data there 
>>> # For various reasons  ,you may want to prevent downloading various files like images or css 
>>> # you can set that like so :
>>> page_report.save("mydata" , download_js = True , download_css = False  , download_images = False )
>>> # in the output  folder , there will be no images or css , only Javascript
>>> # access the data to do something 
>>> page_report.js_urls # urls to javascript files
>>> page_report.css_tags # bs4.Tag instances 

>> help(page_report) # for more info 

```




---



### Crawling a website

```python
# Lets explore a website 
# The 'crawl_limit' kwarg sets the maximum number of pages to crawl , default is 0 which equals to no limit
website_report = explore_website("https://stackoverflow.com"  , crawl_limit = 3 )
# website_report is a crawlfish.WesiteReport instance
# save the report 
website_report.save(output_folder = "WebsiteReport")
# The data will be found in the output folder provided

# For more help :
help(website_report)
help(explore_website)
```



---



### Fetching web pages

```python
>>> from crawlfish import get_page , get_url , get_page_with_driver
>>>
>>> # get a requests.Response object of a page
>>> response = get_page("https://www.sample-videos.com")
Getting page ->  https://www.sample-videos.com DONE
>>>
>>> # get the html of a page
>>> response = get_page("https://www.sample-videos.com")
Getting page ->  https://www.sample-videos.com DONE
>>>
>>> # get the bs4.BeautifulSoup instance fo a page
>>> soup = get_page("https://www.sample-videos.com" , soup = True )
Getting page ->  https://www.sample-videos.com DONE
>>>
>>> # save the page to a file
>>> response = get_page("https://www.sample-videos.com" , output_file = "test_data/stack.html")
Getting page ->  https://www.sample-videos.com DONE
Writing response content to file test_data/stack.htmlDONE
>>>
>>> # Fetch a page with a  selenium webdriver
>>> from selenium import webdriver
>>> from selenium.webdriver.firefox.options import Options
>>> # Initialize your webdriver
>>> options = Options()
>>> options.add_argument("--headless")
>>> driver = webdriver.Firefox(options = options)
>>> html = get_page_with_driver( 'https://www.sample-videos.com' , driver)
Fetching page with driver  <selenium.webdriver.firefox.webdriver.WebDriver (session="9a456c4c-756f-4bc8-a0f9-b973e3ef9a17")> <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
Page HTML fetched successfully
>>>
>>> # Fetch using a selenium webdriver and save a page to a file
>>> html = get_page_with_driver( 'https://www.sample-videos.com' , driver , output_file = "test_data/withdriver.html")
Fetching page with driver  <selenium.webdriver.firefox.webdriver.WebDriver (session="9a456c4c-756f-4bc8-a0f9-b973e3ef9a17")> <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
Page HTML fetched successfully
Writing HTML to file test_data/withdriver.htmlDONE

>>>
>>>
>>> driver.quit()
>>>



```



---




### Downloading files 

- Let's download images , videos and text based files 

```python
>>> from crawlfish import download_images , download_static_code_files , download_video
>>> from crawlfish import download_image , download_static_code_file , download_videos
>>>
>>> # These are some pretty common functions
>>> # use the 'save_to_file' keyword in all of these functions to choose
>>> # whether to save to a file or not
>>>
>>>
>>> # Download an image
>>> file_name , bytes_data = download_image( 'https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg' , output_folder = "test_data/myimages/" )
Getting page ->  https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg DONE
Saving image data to file -------  C:\Users\USER\Documents\GitHub\crawlfish\test_data\myimages\Sample-jpg-image-50kb.jpg  Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\test_data\myimages\Sample-jpg-image-50kb.jpg
DONE
>>> # The image will be saved to the output folder
>>> file_name
'Sample-jpg-image-50kb.jpg'
>>> # Download images from a list of urls
>>> images = ['https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg','https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg']
>>> data =  download_images(images , output_folder = "test_data/my_images") # { file_name:bytes_data.... }
Getting page ->  https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg DONE
Saving image data to file -------  C:\Users\USER\Documents\GitHub\crawlfish\test_data\my_images\Sample-jpg-image-50kb.jpg  Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\test_data\my_images\Sample-jpg-image-50kb.jpg
DONE
Getting page ->  https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg DONE
Saving image data to file -------  C:\Users\USER\Documents\GitHub\crawlfish\test_data\my_images\Sample-jpg-image-100kb.jpg  Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\test_data\my_images\Sample-jpg-image-100kb.jpg
DONE
>>> data.keys()
dict_keys(['Sample-jpg-image-50kb.jpg', 'Sample-jpg-image-100kb.jpg'])
>>>
>>> # lets not save to a file by doing this
>>> file_name , bytes_data = download_image( 'https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg' , save_to_file = False)
Getting page ->  https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg DONE
>>>
>>>
>>>
>>> # Download a video
>>> file_name , bytes_data = download_video('https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4' , output_folder = "test_dat\a/")
Downloading video https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4 --------- DONE
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\test_data\big_buck_bunny_720p_2mb.mp4
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\test_data\big_buck_bunny_720p_2mb.mp4: 3it [00:00,  7.56it/s]
Saving file to  C:\Users\USER\Documents\GitHub\crawlfish\test_data\big_buck_bunny_720p_2mb.mp4 ----------- DONE
>>> # Download videos
>>> videos  = ['https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4' , 'https://www.sample-videos.com/video321/mp4/720/big_bu\ck_bunny_720p_5mb.mp4']
>>> data = download_videos(videos )
Downloading video https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4 --------- DONE
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_2mb.mp4
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_2mb.mp4: 3it [00:00, 540.55it/s]
Saving file to  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_2mb.mp4 ----------- DONE
Downloading video https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_5mb.mp4 --------- DONE
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_5mb.mp4
Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_5mb.mp4: 6it [00:00, 254.32it/s]
Saving file to  C:\Users\USER\Documents\GitHub\crawlfish\big_buck_bunny_720p_5mb.mp4 ----------- DONE
>>>
>>>
>>>
>>> # Download a text file
>>> url = 'https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js'
>>> file_name , text = download_static_code_file(url)
Getting page ->  https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js DONE
saving data to file  C:\Users\USER\Documents\GitHub\crawlfish\jquery.min.js  --------- Writing to file  C:\Users\USER\Documents\GitHub\crawlfish\jquery.min.js
DONE !
>>> file_name
'jquery.min.js'
>>>
>>> # For more info use the help function to read the docstrings
>>>

```



---

## Finding elements

- The method **ElementFinder.find_elements( )** returns a list of all the elements found 
- The items in the list are **bs4.Tag** instances

```python
>>> from crawlfish import ElementFinder
>>> help(ElementFinder) # to get more info that may not be covered here
```


##### Search elements by tag name


```python
>>> from crawlfish import ElementFinder
>>> html = "<h2>Hello</h2> <h2>there </h2> <h2>you</h2>"
>>> finder = ElementFinder(html)
>>> elements = finder.find_elements(tag_name = "h2")
Searching for elements
Finding elements : 100%|████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 4476.31it/s]

 ============ SEARCH COMPLETE ! Found 3 elements that match the search ===========

>>> elements
[<h2>Hello</h2>, <h2>there </h2>, <h2>you</h2>]
```


##### Search elements by tag name , attribute name and attribute value

```python
>>> from crawlfish import ElementFinder
>>> html = """
... <!DOCTYPE html>
... <html>
... <head>
... <title> Let's find elements </title>
... </head>
... <body>
...
... <div></div>
... <div></div>
... <div></div>
... <div id="name" >Sherlock Holmes</div>
... <div id="name" >Mansa Musa</div>
...
...
...
... </body>
... </html>
...
... """
>>> finder = ElementFinder(html)
>>> elements = finder.find_elements( tag_name = "div",  attribute = "id" , attribute_value = "name"  )
Searching for elements
Finding elements : 100%|████████████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:00<00:00, 7232.94it/s]

 ============ SEARCH COMPLETE ! Found 2 elements that match the search ===========

>>> elements
[<div id="name">Sherlock Holmes</div>, <div id="name">Mansa Musa</div>]
>>>
```


##### Search elements by text match

- You can look for elements based on their the text content
- You can also use regex 

```python
>>> # normal text match example
>>> from crawlfish import ElementFinder
>>> html = '<div id="person"> @ ceo Zuck </div> <div id="person">@warlord Khan</div> <div id="person">@ ceo John</div>'
>>> finder = ElementFinder(html)
>>> elements = finder.find_elements( text_match = "ceo" )
Searching for elements
Finding elements : 100%|████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 4505.16it/s]

 ============ SEARCH COMPLETE ! Found 2 elements that match the search ===========

>>> elements
[<div id="person"> @ ceo Zuck </div>, <div id="person">@ ceo John</div>]
>>>
>>> # with regex example
>>> html =  '<div>This is not an email</div> <div>randomemail@yahoo.com</div> <div>anotheremail@gmail.com</div>'
>>> finder = ElementFinder(html)
>>> email_regex = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+"
>>> elements = finder.find_elements(text_match = email_regex)
Searching for elements
Finding elements : 100%|████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 5067.62it/s]

 ============ SEARCH COMPLETE ! Found 2 elements that match the search ===========

>>> elements
```


##### Search elements by tag names , attribute names ,attribute values and text matches

- You can search multiple values at the same time 
- In this example let's look for elements that  contain valid email addresses in their text contents

```python

>>> from crawlfish import ElementFinder
>>>
>>> # Search for elements by multiple values
>>> html = """
... <!DOCTYPE html>
... <html>
... <head>
... <title> Let's find elements </title>
... </head>
... <body>
...
... <div id="person" class="person-container" >
...  Someone had an email and it was someemail@gmail.com , yeah , his name was Ail Someem
...  </div>
...
... <div id="" class="" ></div>
... <div id="" class="" ></div>
... <div id="" class="" ></div>
...
... <div id="" class="email-div" ></div>
...
... <p id="email-p" >validemail@gmail.com</p>
... <p id="email-p" ></p>
... <p id="" class="email-p"></p>
... <p id="" class="email-p"></p>
... <div id="" class="email-div" >Anothervalidemail@gmail.com</div>
... <div id="" class="email-div" ></div>
...
... <p id="" class="email-p"></p>
...
... <a id="" class="" ></a>
... <a id="" class="" ></a>
... <a id="" class="" ></a>
... <a id="" class="" ></a>
... <a id="" class="" ></a>
...


... </body>
... </html>
...
... """
>>> # Lets collect elements with valid email addresses as an example
>>> # You can see the data is jumbled up but there are some constant information we can utilize to get everything in one line
>>> finder = ElementFinder(html)
>>> email_regex = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+"
>>> elements = finder.find_elements(  attributes = [ "id" , "class"] , attribute_values = ['email' , ] ,
...  tag_names = [ 'div' , 'p'] ,text_matches = [email_regex, ]    )
Searching for elements
Finding elements : 100%|███████████████████████████████████████████████████████████████████████████████████████████| 21/21 [00:00<00:00, 412.95it/s]

 ============ SEARCH COMPLETE ! Found 3 elements that match the search ===========

[<div class="person-container" id="person">
 Someone had an email and it was someemail@gmail.com , yeah , his name was Ail Someem
 </div>, <p id="email-p">validemail@gmail.com</p>, <div class="email-div" id="">Anothervalidemail@gmail.com</div>]
>>> elements
>>> [<div class="person-container" id="person">
 Someone had an email and it was someemail@gmail.com , yeah , his name was Ail Someem
 </div>, <p id="email-p">validemail@gmail.com</p>, <div class="email-div" id="">Anothervalidemail@gmail.com</div>]
```




---



## Using the UrlsCrawler class

- The UrlsCrawler class is used when one want to scrape  urls in an iterable or in a file containing the urls line by line
- Here is an example

```python

>>> from crawlfish import UrlsCrawler , ExcelSaveOption , CSVSaveOption ,JSONSaveOption ,JSONFileSaveOption
>>> # The UrlsCrawler class lghtens the load for developers when scraping from a list of links
>>> # or from a text file containing the links
>>>
>>> # Lets say we have a function for scraping a url
>>> def scrape_url(url):
...     data = ["23" , "John" , "john@gmail.com"]
...     return data
...
>>>
>>>
>>> # now create the headers for our data
>>> headers = [ 'AGE' , 'NAME' , 'EMAIL' ]
>>> urls = ["url1" , "url2","url3"]
>>>
>>>
>>>
>>> # create a save option to customize how you want your data saved
>>> save_option = CSVSaveOption(file = "test_data/data.csv" , overwrite = True , delimiter = ",")
>>> # lets get our data
>>> data = UrlsCrawler().scrape_urls(  urls = urls  , scrape_function = scrape_url ,
...  data_headers = headers ,save_option =save_option)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 8050.49it/s]
>>> # The data will be saved to a the file provided
>>> with open("test_data/data.csv") as f:
...     print(f.read())
...
AGE,NAME,EMAIL
23,John,john@gmail.com
23,John,john@gmail.com
23,John,john@gmail.com

>>>
>>> #Scrape links from a file with the links line by line
>>> links_file = "test_data/links.txt"
>>> data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
... data_headers  =headers , save_option = save_option )
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 8366.30it/s]
>>>
>>>
>>> # Save to different formats
>>> # you can use the different save options like so :
>>>
>>> # excel spreasheet save option
>>> ExcelSaveOption( "myfile.xlsx" , sheet_name = "sheetA" ,overwrite = False )
<crawlfish.crawler.save_options.ExcelSaveOption object at 0x0000000005EDD090>
>>>
>>> # to return the data as dict in the format { index_header:{key:data , key:data}........ }
>>> # key_index is the index of an item in the scrape function result that will be used as the main key if the data is
>>> # to be saved in a dictionary-like form
>>> ave_option = JSONSaveOption(key_index = 2 )
>>> data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
... data_headers  =headers , save_option = save_option )
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 8272.79it/s]
>>> data
[['23', 'John', 'john@gmail.com'], ['23', 'John', 'john@gmail.com'], ['23', 'John', 'john@gmail.com']]
>>>
>>>
>>> # To save to  a .JSON file
>>> save_option =JSONFileSaveOption( 'test_data/myfile.json' , key_index = 2 , overwrite = True )
>>> data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
... data_headers  =headers , save_option = save_option )
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 4667.25it/s]
>>> data
[['23', 'John', 'john@gmail.com'], ['23', 'John', 'john@gmail.com'], ['23', 'John', 'john@gmail.com']]
```



---


## Using the ListDataSaver class

- When you have a list containig lists that have the same length , you can use this function to flexibly save the data in different file formats
- Here's how to go about that

```python
>>> from crawlfish import ListDataSaver
>>>
>>> # This is just a class  that may come in handy  when you want to save data
>>> # that is in a list
>>>
>>> data = [
... ["Mike" , "alburqueque" , "herewhatsgonnahappen@gmail.com",],
... ["Jesse" , "alburqueque" , "thebomb_yo#gmail.com"],
... ["Tuco Salamanca" , "Mexico" , "youpunkinme@gmail.com"],
... ]
>>>
>>> headers = [ "name" , "address" , "email" ]
>>> saver = ListDataSaver()
>>> # remember to add you headers at the start of the data list
>>> data = [headers,] + data
>>>
>>> # save to csv
>>> saver.to_csv_file(data ,   "test_data/myfile.csv" ,overwrite = False)
[['name', 'address', 'email'], ['Mike', 'alburqueque', 'herewhatsgonnahappen@gmail.com'], ['Jesse', 'alburqueque', 'thebomb_yo#gmail.com'], ['Tuco Salamanca', 'Mexico', 'youpunkinme@gmail.com']]
>>>
>>> # save to spreadsheet
>>> saver.to_spreadsheet_file( data , 'test_data/file.xlsx' , overwrite = True )
[['name', 'address', 'email'], ['Mike', 'alburqueque', 'herewhatsgonnahappen@gmail.com'], ['Jesse', 'alburqueque', 'thebomb_yo#gmail.com'], ['Tuco Salamanca', 'Mexico', 'youpunkinme@gmail.com']]
>>>
>>> # save to json
>>> json_format = saver.to_json(data , key_index = 2)
0 ['name', 'address', 'email']
1 ['name', 'address', 'email']
0 ['name', 'address', 'email']
1 ['name', 'address', 'email']
0 ['name', 'address', 'email']
1 ['name', 'address', 'email']
>>> json_format
{'herewhatsgonnahappen@gmail.com': {'name': 'Mike', 'address': 'alburqueque'}, 'thebomb_yo#gmail.com': {'name': 'Jesse', 'address': 'alburqueque'}, 'youpunkinme@gmail.com': {'name': 'Tuco Salamanca', 'address': 'Mexico'}}
>>>
>>>
>>> # save to json file
>>> file = "test_data/data.json"
>>> saver.to_json_file( data , key_index = 1 , file = file ,overwrite = True , indent = 4 )
0 ['name', 'address', 'email']
2 ['name', 'address', 'email']
0 ['name', 'address', 'email']
2 ['name', 'address', 'email']
0 ['name', 'address', 'email']
2 ['name', 'address', 'email']
{'alburqueque': {'name': 'Jesse', 'email': 'thebomb_yo#gmail.com'}, 'Mexico': {'name': 'Tuco Salamanca', 'email': 'youpunkinme@gmail.com'}}
>>> with open(file , "r") as f:
...     print(f.read())
...
{
    "alburqueque": {
        "name": "Jesse",
        "email": "thebomb_yo#gmail.com"
    },
    "Mexico": {
        "name": "Tuco Salamanca",
        "email": "youpunkinme@gmail.com"
    }
}
>>>






```




---


#### Using your own custom functions to fetch urls

- Crawlfish allows for you to use your own funtions for fetching urls , by default it has its own functions for fetching urls so no need to bother changing unless you really need to .
- These functions are expected to take a **url string**  (eg https//somesite.com ) as an argument and return a ***requests.Response*** object
- Here are some usage instances just to give you an idea ,I recommend using the inbuilt  ***help()*** function if you get stuck



```python


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




```






##### Thanks for reading , or installing or whatever . Have a good one. Cheers !

![Adios! ](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3J4NzA1YmdmeHFzMzMxdzI4N3Vka2t4cDI2OXY0dTNncmdwZTlmOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12xvz9NssSkaS4/giphy.gif)

