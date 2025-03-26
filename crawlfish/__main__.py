import os 
import sys 
import art
import argparse
from ascii_magic import AsciiArt 
from crawlfish import  crawler , supported
from crawlfish import crawlfish_utils



base_dir = os.path.split(os.path.abspath(__file__))[0]



def exit_program():
	''' For exiting all processes
	'''
	print("-------------- EXITING ---------------")
	sys.exit()


def check_option_urls(urls):
	'''a helper function that ensures the validity of the url(s) provided . Exits the program if a url is invalid'''
	for u in urls :
		if not u.startswith("https"):
			print("Invalid url provided - ", u)
			exit_program()


def get_urls_from_file(file:str):
	print("Collecting urls from file , ", file )
	if not crawlfish_utils.check_file(file , make_if_none = False):
		print("Invalid file path provided . Please make sure that file exists ")
		exit_program()
	urls_in_file = []
	urls = []
	with open(file , "r") as f:
		urls_in_file = f.readlines()
	for u in urls_in_file:
		u = u.strip().replace("\n" , '')
		if u == "":
			continue
		urls.append(u)
	if len(urls) == 0 :
		print("No urls found in file " , file)
		exit_program()
	check_option_urls(urls)
	return urls




logo_image = os.path.join(base_dir , "package_data/images/logo.png")

logo = art.text2art("Crawlfish"  ,font = "stforek")
print(logo)
intro = """

by Victor Kipkemboi | scriptilapia@gmail.com

====================================================================================================================
""".format()
print(intro)



# ARGUMENTS
parser = argparse.ArgumentParser()

work_to_do = parser.add_mutually_exclusive_group( )
work_to_do.add_argument("-d","--download",action = "store_true" , help = "Download a file or files")
work_to_do.add_argument("-cp","--crawl-page",action = "store_true" , help = "Crawl a webpage or webpages")
work_to_do.add_argument("-cs","--crawl-site",action = "store_true" , help = "Crawl a website or websites")

# CRAWLING OPTIONS 
parser.add_argument("-rs", "--redownload-static"  ,action="store_true" , 
			help ="""This option present means that  static files with similar urls from different web pages will be downloaded evertime they are found instead of caching the data since they are most likely similar.  """)

# URL(s) INPUT
parser.add_argument("-u" ,"--url" , help = "The URL(s) you want to process . Make sure to add spaces in between the urls" , nargs = "*" )
parser.add_argument("-uf" ,"--urls-file" , help = "The path or name of a file containing urls to be processed  " )

# FILE FORMATS TO DOWNLOAD
download_formats = parser.add_mutually_exclusive_group()
download_formats.add_argument("-i","--image", action="store_true", help = "Indicate that you are downloading an image. Eg: .png ,  .jpeg , .jpg ")
download_formats.add_argument("-v", "--video", action="store_true", help = "Indicate that you are downloading a video. Eg: .mp4 , .mp3 , .mkv ....")
download_formats.add_argument("-tf", "--text-file",action="store_true",  help="Indicate that you are downloading a text-based file . Eg: .js, .txt , .css")

# STATIC FILES TO NOT DOWNLOAD 
parser.add_argument("-es" , '--exclude-static' ,
					 help = "Static file to not download during crawling processes . This option will have no effect during downloading " , 
					 nargs = "*", 
					 choices = supported.CRAWL_STATIC_TYPES,
					 default = [], 
					)


# OUTPUT DATA STORAGE
output_storage = parser.add_mutually_exclusive_group()
output_storage.add_argument("-f", "--file" , help = """The name to be given to the FILE you want to download. Has no effect when many url(s) are downloaded . Make sure to include the correct extension for convenience""" )
output_storage.add_argument("-fn", "--file-name" ,
				 help = """The name you want to give to the downloaded file . The extension will be added automatically .
				  To be used only when one url has been provided otherwise it has no effect whatsoever"""
				  )
output_storage.add_argument("-outd", "--output-dir" , help= "The directory where you want your output stored . The current directory will be used if none is provided . If the process has no use for this , it will have no effect " )


# LIMITS 
parser.add_argument('-cl' , '--crawl-limit' , 
	help = "The number of maximum urls to crawl when crawling a website or a webpage . 0 = Infinity , the default is 0 . This option takes effect during site crawling only" , 
	type = int , 
	default = 0)

args = parser.parse_args()






print("Starting ------------------------- ")
# prepare output storages
output_folder = os.getcwd()
if args.output_dir:
	output_folder = args.output_dir
urls = []
output_file = None 

if args.url:
	check_option_urls(args.url)
	urls = args.url 
elif args.urls_file:
	urls = get_urls_from_file(args.urls_file)

if urls:
	print("{} url(s) waiting to be processed".format(len(urls)))
else:
	print("NO Urls provided :( ")
	exit_program()
# PROCESS ARGUMENTS 
if args.download:
	print("Downloading {} items ".format(len(urls)) )
	if args.image:
		if len(urls) == 1:
			crawler.download_image(urls[0] , file = args.file , file_name = args.file_name , output_folder = output_folder)
		else:
			crawler.download_images(urls , output_folder = output_folder)
	# download videos(s)
	elif args.video:
		if len(urls) == 1:
			crawler.download_video(urls[0] , file = args.file , file_name = args.file_name , output_folder = output_folder)
		else:
			crawler.download_videos(urls , output_folder = output_folder)
	# download text based files
	elif args.text_file:
		if len(urls) == 1:
			crawler.download_static_code_file(urls[0] , file = args.file , file_name = args.file_name , output_folder = output_folder)
		else:
			crawler.download_static_code_files(urls , output_folder = output_folder)
	print("Process complete !")


elif args.crawl_site:
	print("Crawling {} website(s)".format(len(urls)))
	website_reports= []
	for u in urls :
		report = crawler.explore_website(u , crawl_limit = args.crawl_limit)
		website_reports.append(report)
	for wr in website_reports:
		print("Saving website report " , wr )
		wr.save( output_folder = output_folder , redownload_static = args.redownload_static , exclude_static = args.exclude_static )
	print("Process complete !")

elif args.crawl_page:
	print("Crawling webpage(s)")
	webpage_reports = [] 

	for u in urls :
		page_report  =crawler.explore_webpage(u)
		webpage_reports.append(page_report)
	print("Saving web page reports ----- ")
	download_images  ,download_js , download_css = False if 'img' in args.exclude_static else True  , False if 'js' in args.exclude_static else True  , False if 'css' in args.exclude_static else True  
	for pr in webpage_reports:
		pr.save( output_folder = output_folder , download_css = download_css , download_js = download_js  , download_images = download_images )

	print("Process complete !")