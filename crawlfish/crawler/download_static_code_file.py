import os 
from types import FunctionType
from collections.abc import Iterable
import requests
from tqdm import tqdm 
from crawlfish.http import get_url
from crawlfish.crawlfish_utils import check_file , check_folder
from .extract_file_info_from_url import extract_file_info_from_url

def download_static_code_file(
	url:str ,
	get_function:FunctionType = get_url ,
	file:str = '' ,
	output_folder:str = os.getcwd(),
	encoding:str = 'utf-8' ,
	file_name:str = '' ,
	save_to_file:bool = True
	):

	'''Downloads a static text based file eg "https:fie.js" and saves it to the file path provided if save_to_file =True

	Parameters
	----------
	url:str
		The URL of the file to be  downloaded
	get_function:FunctionType
		A function that takes a url as a parameter and returns a request.Response object 
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
		(file_name,data .....)
'''
	response = get_function(url)
	text = response.text
	url_file_name ,extension = extract_file_info_from_url(url)
	if output_folder:
		output_folder = os.path.abspath(output_folder)
		check_folder(output_folder)
	if output_folder and not file and not file_name:
		file= os.path.join(output_folder , url_file_name )
	if file_name:
		file_name += extension
		file = os.path.join(output_folder , file_name )
	if not file_name:
		file_name = os.path.split(file)[-1]
	if save_to_file:
		print("saving data to file ", file , ' --------- ' , end = '')
		if not check_file(file):
			return file_name ,''
		with open(file , "w" ,encoding = encoding) as f:
			f.write(text)
		print("DONE !")
	return file_name , text

def download_static_code_files(
	urls_list:Iterable,
	get_function = get_url ,
	output_folder = os.getcwd(),
	encoding = 'utf-8'
	):
	'''Downloads text based files from the urls provided in the urls_list

	Parameters
	----------
	urls_list:Iterable 
		An iterable containing the urls of the text-based files to be downloaded
	get_function:FunctionType
		A function that takes a url as an argument and returns a request.Response object 
	output_folder:str
		The folder/directory where to store the downloaded files

	Returns
	-------
	files_data:dict
		{ filename:text_data , ...... }
		A dictionary containing the text data as values and file names as keys
	'''

	files_data = {}
	for url in tqdm(urls_list):
		file_name , data = download_static_code_file(url , get_function = get_function , output_folder  = output_folder, encoding = encoding)
		files_data[file_name] = data
	return files_data