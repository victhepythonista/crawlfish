import os 


def extract_file_info_from_url(url:str):
	'''This funtion extracts the name and extension name of a file from a url 

	'https:site.com/file.mp4?key=djhfjddata=45'

		will return :

	 'file.mp4' , '.mp4' 

	 Parameters
	 ----------
	 url:str
	 	The url to extract from"""
	Returns
	-------
	tuple
		The data extracted in this format: 
			(file_name , extension)	
	'''
	split = url.split("/")
	file_name =split[-1]
	file_name = file_name.split("?")[0]
	extension = os.path.splitext(file_name)[-1]
	return file_name , extension