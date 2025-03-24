# TEST DATA FOR UUH, TESTING 

import os 
from bs4 import BeautifulSoup



base_dir = os.path.split(os.path.abspath(__file__))[0]

def read_file(file):
	data = ''
	file = os.path.join(base_dir , file)
	with open(file , 'r') as f:
		data = f.read()
	return data

make_soup = lambda html: BeautifulSoup(html , "html.parser")


test_extract_meta_soup  = make_soup( read_file("test_extract_meta_soup.html"))

grocery_list_soup = make_soup( read_file("grocery_list.html"))
elements_to_find_soup = make_soup( read_file("test_elements_to_find.html"))
test_internal_static_soup = make_soup(read_file("test_internal_static_code.html"))
