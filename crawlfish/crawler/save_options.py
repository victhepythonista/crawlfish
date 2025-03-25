from crawlfish.crawler.exceptions import InvalidSaveOptionError  
from save_formats  import save_formats




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
		self.save_format = save_formats.JSON_FILE
		self.key_index = key_index 
		self.ensure_ascii = ensure_ascii
		self.encoding = encoding
		self.indent = indent
		self.file = file 
		self.overwrite = overwrite
		


 