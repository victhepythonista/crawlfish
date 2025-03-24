import os 


def check_file(file_path:str , make_if_none:bool = True  ,encoding:str = "utf-8"):
	'''
	 check if the path exists and if specified ,  attempts to create it and return True 

	Parameters
	-----------
	file_path:str
		The file path to check
	make_if_none:bool
		Whether or not to try and make he file if it doesnt exist
	encoding:str
		The encodng to use when attempting to create the file 

	Returns
	-------
	bool
		Whether or not the file exists
	'''
	folder  , file = os.path.split(file_path)
	if not make_if_none:

		return os.path.isfile(file_path)
	# print("Will make if none")
	if os.path.isfile(file_path):
		return True 
	if not file:
		return False
	if not os.path.isdir(folder) and folder.strip() != ''  :
		try:
			os.makedirs(folder)
		except Exception as e:
			print("Could not make file folder "  , 'because of error ', e)
			return False
	print("Writing to file " , file_path)
	try:
		with open(file_path , "w" , encoding = encoding) as f:
			f.write("")
	except (ValueError ,OSError) as e:
		return False
	except Exception as e:
		raise
	return os.path.isfile(file_path)