import os
from collections.abc import Iterable
import requests
import tldextract 
from tqdm import tqdm 
from crawlfish.crawlfish_utils import check_file ,check_folder
from .extract_file_info_from_url import extract_file_info_from_url




def download_video( 
	url:str ,
	output_folder:str = os.getcwd()   , 
	file:str = "" ,
	file_name:str = "",
	save_to_file:bool = True
	):
	'''This function downloads a video from the provided url  returns the bytes  data and save the data to a file if save_to_file=True
	Parameters
	----------
	url:str
		The URL of the video file to be  downloaded
	file:str
		The name of the file to write the downloaded data to 
	output_folder:str
		The folder/directory where to store the downloaded file 
	save_to_file:bool
		Whether or not to save the data to a file 
	file_name:
		The name of the file withholding the extension name where the downloaded data will be written .
		The extension will be added automatically if this is  provided 

	Returns
	-------
	tuple 
		(file_name,bytes_data .....)
	'''
	print("Downloading video {} --------- ".format(url) , end =''  )
	response = requests.get(url, stream = True)
	print("DONE") 
	content = response.content
	url_file_name ,extension = extract_file_info_from_url(url)
 
	if output_folder:
		output_folder = os.path.abspath(output_folder)
		check_folder(output_folder)
	if output_folder and not file and not file_name:
		file= os.path.join(output_folder , url_file_name )
	if file_name:
		file_name += extension
		file = os.path.join(output_folder , file_name  )
	if not file_name:
		file_name = os.path.split(file)[-1]
	if not save_to_file:
		return file_name , response.content 
	# write the data 
	if not check_file(file):
		return file_name , b''
	print("Saving file to " , file , '----------- ', end = '')
	with open(file, 'wb') as f: 
		for chunk in tqdm(response.iter_content(chunk_size = 1024*1024), 'Writing to file  {}'.format(file)): 
			if chunk: 
				f.write(chunk)
		print("DONE")
	return file_name , content


def download_videos(
	urls_list:Iterable ,
	output_folder:str = os.getcwd()
	    ):
	''' This functions downloads videos from a list of urls and return the data in a dict
	Parameters
	----------
	urls_list:Iterable,tuple,iter,set
		An iterable containing the urls of the text-based files to be downloaded
	output_folder:str
		The folder/directory where to store the downloaded files

	Returns
	-------
	files_data:dict
		{ filename:text_data , ...... }
		A dictionary containing the text data as values and file names as keys'''
	video_data = {}
	for url in urls_list:
		file_name , data = download_video(url , output_folder = output_folder)
		video_data[file_name] = data
	return video_data

