

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
	def __init__(self , file  , overwrite = True , delimiter=','):
		SaveOption.__init__(self)
		self.file = file 
		self.overwrite = overwrite
		self.save_format = save_formats.CSV_FILE
		self.delimiter = delimiter





class ExcelSaveOption(SaveOption):
	def __init__(self , file , sheet_name , overwrite = True):
		SaveOption.__init__(self)
		self.file = file 
		self.sheet_name = sheet_name 
		self.overwrite = overwrite
		self.save_format = save_formats.EXCEL_FILE

class JSONSaveOption(SaveOption):
	def __init__(self , key_index = 0 ):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 

class JSONFileSaveOption(SaveOption):
	def __init__(self ,file ,  key_index = 0 ,overwrite = True, ensure_ascii = False  , indent = 4 , encoding = 'utf-8' ):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 
		self.ensure_ascii = ensure_ascii
		self.encoding = encoding
		self.indent = indent
		self.file = file 
		self.overwrite = overwrite
		

class InvalidSaveOptionError(Exception):
	''' To be raised when an object is not a SaveOption object '''
	def __init__(self , message):
		self.message = "Crawlfish could not load this SaveOption class -> " +  message
		super().__init__(self.message)


