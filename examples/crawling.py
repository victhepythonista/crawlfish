from crawlfish import explore_webpage , explore_website 


# Lets expore a web page 
page_report = explore_webpage("https://stackoverflow.com")
# returns a crawlfish.WebpageReport object 




# Save the scraped data 
page_report.save( output_folder = "mydata" )
# a folder named my data will be created and youll find all the data there 

# For various reasons  ,you may want to prevent downloading various files like images or css 
# you can set that like so :
page_report.save("mydata" , download_js = True , download_css = False  , download_images = False )
# in the output  folder , there will be no images or css , only Javascript

# access the data to do something 
page_report.js_urls # urls to javascript files
page_report.css_tags # bs4.Tag instances 

help(page_report) # for more info 


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
