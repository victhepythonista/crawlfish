import os 


def check_folder(folder:str):
	''' CHecks if a folder exists and tries to create if it if not .Returns an error if the foldr couldnt be created


	Parameters
	----------
	folder:str
		The name of the folder to check 



	Returns
	-------
	bool
		Whether or not  the folder finally  exists or not 
		'''

 
	if not os.path.isdir(folder)  :
		try:
			os.makedirs(folder)
			return True
		except:
			raise 
		return False
	return True