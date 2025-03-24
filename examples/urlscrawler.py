from crawlfish import UrlsCrawler , ExcelSaveOption , CSVSaveOption ,JSONSaveOption ,JSONFileSaveOption
# The UrlsCrawler class lghtens the load for developers when scraping from a list of links 
# or from a text file containing the links 

# Lets say we have a function for scraping a url
def scrape_url(url):
	data = ["23" , "John" , "john@gmail.com"]
	return data



# now create the headers for our data 
headers = [ 'AGE' , 'NAME' , 'EMAIL' ]
urls = ["url1" , "url2","url3"] 



# create a save option to customize how you want your data saved
save_option = CSVSaveOption(file = "test_data/data.csv" , overwrite = True , delimiter = ",")
# lets get our data
data = UrlsCrawler().scrape_urls(  urls = urls  , scrape_function = scrape_url ,
		 data_headers = headers ,save_option =save_option)
# The data will be saved to a the file provided
with open("test_data/data.csv") as f:
	print(f.read())


#Scrape links from a file with the links line by line
links_file = "test_data/links.txt"
data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
			data_headers  =headers , save_option = save_option )


# Save to different formats
# you can use the different save options like so :

# excel spreasheet save option
ExcelSaveOption( "myfile.xlsx" , sheet_name = "sheetA" ,overwrite = False )

# to return the data as dict in the format { index_header:{key:data , key:data}........ }
# key_index is the index of an item in the scrape function result that will be used as the main key if the data is
# to be saved in a dictionary-like form
ave_option = JSONSaveOption(key_index = 2 )
data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
			data_headers  =headers , save_option = save_option )
data


# To save to  a .JSON file 
save_option =JSONFileSaveOption( 'test_data/myfile.json' , key_index = 2 , overwrite = True )
data  = UrlsCrawler().scrape_urls_in_file( links_file , scrape_function = scrape_url ,
			data_headers  =headers , save_option = save_option )
data