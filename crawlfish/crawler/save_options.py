from crawlfish.crawler.exceptions import InvalidSaveOptionError  

class save_formats:
	'''
	For representing the save format for scraped data 
	The attributes just act as quick to access identifiers for the save type when only the save type is needed


	''' 

	EXCEL_FILE = "EXCEL_SPREADSHEET_FORMAT"
	CSV_FILE = "CSV_FORMAT"
	JSON  = "jSON OBJECT"
	JSON_FILE = "JSON FILE " 
	STATIC_CODE = "JAVASCRIPT_OR_CSS_CODE"
	IMAGE = "PNGs, JPEGS ....."




class SaveOption:
	"""
	A base class for specifying how scraped data is to be saved
	"""
	save_format = ""
	def __init__(self):
		pass 


class CSVSaveOption(SaveOption):
	def __init__(self , file:str , overwrite:bool = True , delimiter:str=','):
		SaveOption.__init__(self)
		self.file = file 
		self.overwrite = overwrite
		self.save_format = save_formats.CSV_FILE
		self.delimiter = delimiter


 


class ExcelSaveOption(SaveOption):
	def __init__(self , file:str , sheet_name:str , overwrite:bool = True):
		SaveOption.__init__(self)
		self.file = file 
		self.sheet_name = sheet_name 
		self.overwrite = overwrite
		self.save_format = save_formats.EXCEL_FILE

class JSONSaveOption(SaveOption):
	def __init__(self , key_index:int = 0 ):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 

class JSONFileSaveOption(SaveOption):
	def __init__(self ,file ,  key_index:int = 0 ,
				overwrite:bool = True,
				 ensure_ascii:bool = False  ,
				 indent:int = 4 , 
				 encoding:str = 'utf-8' ):
		self.save_format = save_formats.JSON 
		self.key_index = key_index 
		self.ensure_ascii = ensure_ascii
		self.encoding = encoding
		self.indent = indent
		self.file = file 
		self.overwrite = overwrite
		


 