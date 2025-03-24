


def ensure_html_url(url:str):
	'''Returns a boolean indicating if the url looks like it leads to a html page ,
		ie .The content-type of the request headers will be 'text/html'

	Parameters
	----------
	url:str
		The url to check

	Returns
	-------
	bool
		Whether the url is valid or not 
	'''

	url = url.split('?')[0].lower()
	if not url.startswith('http'):
		return False
	unwanted_ends = ['.jpg' ,'.png' , '.jpeg' , '.jpg','.gif','.svg',

						'.css','.js', '.scss','.json', 
						'.3gp','.mp4a', '.mp4' , 'mp3', '.avi' , '.mkv' ,'.flv' , 
						'.pdf', '.zip' , '.psd' , '.dxf' , '.doc' , '.docx','.ppt','.sql','xlsx','xls', ]
	for unwanted in unwanted_ends:
		if url.endswith(unwanted):
			return False
	return True 