

class save_formats:
	'''
	For representing the save format for scraped data 
	''' 

	EXCEL_FILE = "EXCEL_SPREADSHEET_FORMAT"
	CSV_FILE = "CSV_FORMAT"
	JSON  = "jSON OBJECT"
	JSON_FILE = "JSON FILE " 




class SaveOption:
	"""
	A base class for specifying how scraped data is to be saved
	"""
	save_format = ""
	def __init__(self):
		pass 



class CSVSaveOption(SaveOption):
	def __init__(self , file  , overwrite = True):
		SaveOption.__init__(self)
		self.file = file 
		self.overwrite = overwrite
		self.save_format = save_formats.CSV_FILE





class ExcelSaveOption(SaveOption):
	def __init__(self , file , sheet_name , overwrite = True):
		SaveOption.__init__(self)
		self.file = file 
		self.sheet_name = sheet_name 
		self.overwrite = overwrite
		self.save_format = save_formats.EXCEL_FILE

class JsonSaveOption(SaveOption):
	def __init__(self , key_index):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 

class JsonFileSaveOption(SaveOption):
	def __init__(self ,file ,  key_index):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 
		self.file = file 
		
