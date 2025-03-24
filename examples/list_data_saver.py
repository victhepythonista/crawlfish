from crawlfish import ListDataSaver

# This is just a class  that may come in handy  when you want to save data 
# that is in a list 

data = [
	["Mike" , "alburqueque" , "herewhatsgonnahappen@gmail.com",],
	["Jesse" , "alburqueque" , "thebomb_yo#gmail.com"],
	["Tuco Salamanca" , "Mexico" , "youpunkinme@gmail.com"],
	]

headers = [ "name" , "address" , "email" ]
saver = ListDataSaver()
# remember to add you headers at the start of the data list 
data = [headers,] + data 

# save to csv
saver.to_csv_file(data ,   "test_data/myfile.csv" ,overwrite = False)

# save to spreadsheet
saver.to_spreadsheet_file( data , 'test_data/file.xlsx' , overwrite = True )

# save to json 
json_format = saver.to_json(data , key_index = 2)
json_format


# save to json file
file = "test_data/data.json"
saver.to_json_file( data , key_index = 1 , file = file ,overwrite = True , indent = 4 )
with open(file , "r") as f:
	print(f.read())
