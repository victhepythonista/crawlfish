import requests
import os
from types import FunctionType
from urllib.request import urlopen
from crawlfish.crawlfish_utils import check_folder ,check_file
from crawlfish.http import get_url
from .extract_file_info_from_url import extract_file_info_from_url

def download_image(
	url:str ,
	get_function:FunctionType = get_url ,
	file:str = '' ,
	output_folder:str = os.getcwd() , 
	file_name:str = '' ,
	save_to_file:bool = True
	):

	'''Downloads an image file from a url , returns the image data and saves the image to a file if save_to_file=True

	Parameters
	----------
	url:str
		The URL of the image to want to download
	get_function:FunctionType
		A function that takes the url as a parameter and returns a request.Response object 
	file:str
		The name of the file to write the downloaded data to 
	output_folder:str
		The folder/directory where to store the downloaded file 
	save_to_file:bool
		Whether or not to save the data to a file 
	file_name:
		The name of the file withholding the extension name where the downloaded data will be written .
		The extension will be added automatically if this is provided 


	Returns
	-------
	tuple 
		(file_name,image_data)


	'''
	response = get_function(url)
	content =response.content
	url_file_name , extension = extract_file_info_from_url(url)
	if output_folder:
		output_folder = os.path.abspath(output_folder)
		check_folder(output_folder)
	if output_folder and not file and not file_name:
		file =os.path.join(output_folder , url_file_name)
	if file_name:
		file_name  = file_name + extension
		file = os.path.join(output_folder , file_name)
	if not file:
		file  = os.path.join(output_folder , url_file_name)
	if not file_name:
		file_name = os.path.split(file)[-1]
	if save_to_file:
		print("Saving image data to file ------- ", file ,' ', end = '')
		if not check_file(file  ):
			print("Could not save to file :( " , file)
			return file_name , ''
		with open(file , "wb" ) as f:
			f.write(content)
		print("DONE")	
	return file_name , content

def download_images(urls_list:tuple[list,tuple,iter,set], get_function = get_url ,
						 output_folder = os.getcwd()):
	'''Downloads images from a list of urls and returns the content and data of the images in a list 
	

	Parameters
	----------
	urls_list:list,tuple,iter,set
		An iterable containing the uruuls of the images to be downloaded
	get_function:FunctionType
		A function that takes a url as an argument and returns a request.Response object 
	output_folder:str
		The folder/directory where to store the downloaded files

	Returns
	-------
	image_data:dict
		{ filename:bytes_data , ...... }
		A dictionary containing the image data as values and file names as keys
	'''

	image_data ={}
	for url in urls_list:
		file_name , data = download_image(url , get_function = get_function , output_folder = output_folder)
		image_data[file_name] = data 
	return image_data

