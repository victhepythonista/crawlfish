import os , csv  , json , openpyxl
from openpyxl import Workbook



def check_file(file_path):
	# checl if the path exists and attempts to create it if non existent 
	if os.path.isfile(file_path):
		return True 
	folder  , file = os.path.split(file_path)
	if not os.path.isdir(folder):
		os.makedirs(folder)
	with open(file_path , "w") as f:
		f.write("")
	return os.path.isfile(file_path)

class ScrapedDataSaver:
	'''
	This class contains methods for saving scraped data in different file formats

	'''
	@staticmethod
	def to_csv_file(  data:list , file:str = "Scraped_data.csv" , overwrite = True):
		'''Saves data to  CSV file '''
		data = data 
		if not check_file(file):
			raise FileNotFoundError("Could not write to file - {}".format(file))
		# try and get existing data 
	 

		with open(file , "w" , newline= '') as f:
			writer = csv.writer(f )
			for row in data:
				writer.writerow(row)



	@staticmethod 
	def to_spreadsheet_file(data:list , file:str , sheet_name = "data" , overwrite = True):
		'''Saves data to an excel spreadheet file . 
		The program will not overwite existing data provide that a unique sheet name id provided
		'''
		data = data 
		if not check_file(file):
			return FileNotFoundError("Could not create or write to file - {}".format(file))
		# try and get existing data 
		workbook = ""
		sheet = ""
		file_size = os.path.getsize(file)

		if file_size > 0:
			# file contains something maybe 
			try:
				workbook = openpyxl.load_workbook(file)
			except:
				raise 
		if not workbook:
			workbook = Workbook()
		if sheet_name in workbook.sheetnames:
			if overwrite:
				del workbook[sheet_name]
				sheet = workbook.create_sheet(sheet_name)
			else:
				# remove the header from data since we are now appending to existing data 
				if len(data) > 1:
					data = data[1:]
				else:
					data = []
				sheet = workbook[sheet_name]
		else:
			sheet = workbook.create_sheet(sheet_name)
		for row in data:
			sheet.append(row)
		workbook.save(file)


	@staticmethod
	def to_dict(data:list , key_index:int):
		'''Converts the data to a dict object
		
		Parameters
		----------
		'''
		data_in_dict_form ={}
		headers = data[0]
		for row in data:
			if data.index(row) == 0:
				continue
			header = row[key_index]
			value = {}
			for item in row:
				index  = row.index(item)
				if index == key_index:
					continue
				value[headers[index]] = item 
			data_in_dict_form[header] = value 
		return data_in_dict_form



	@staticmethod
	def to_json(data:list , key_index = 0 ):
		'''Converts the data to a json object'''
		data_in_dict_form = ScrapedDataSaver.to_dict(data , key_index = key_index)
		json_obj = json.dumps(data_in_dict_form)
		return json_obj 

	@staticmethod
	def to_json_file(data:list , key_index = 0, file:str = "scraped_data.json" , overwrite = True, ensure_ascii = False  , indent = 4 ):
		'''Converts the data to a json object'''
		if not check_file(file):
			raise FileNotFoundError("Could not load or write to file :( ")
		data_in_dict_form = ScrapedDataSaver.to_dict(data , key_index = key_index)
		existing_json = ""
		try:
			with open(file , "r")  as f:
				existing_json = json.load(f)
		except (UnicodeDecodeError , json.JSONDecodeError) as e :
			pass 
		except:
			raise
		data_to_write = {}
		if overwrite:
			data_to_write = data_in_dict_form
		else:
			data_to_write = existing_json | data_in_dict_form
		with open(file, 'w', encoding='utf-8') as f:
			json.dump(data_to_write, f, ensure_ascii=ensure_ascii, indent=indent)
		return json.dumps(data_in_dict_form)
	