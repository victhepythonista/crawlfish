from crawlfish import download_images , download_static_code_files , download_video 
from crawlfish import download_image , download_static_code_file , download_videos 

# These are some pretty common functions 
# use the 'save_to_file' keyword in all of these functions to choose 
# whether to save to a file or not


# Download an image
file_name , bytes_data = download_image( 'https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg' , output_folder = "test_data/myimages/" )
# The image will be saved to the output folder
file_name
# Download images from a list of urls
images = ['https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg','https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg']
data =  download_images(images , output_folder = "test_data/my_images") # { file_name:bytes_data.... }
data.keys()

# lets not save to a file by doing this
file_name , bytes_data = download_image( 'https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg' , save_to_file = False)



# Download a video 
file_name , bytes_data = download_video('https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4' , output_folder = "test_data/")
# Download videos
videos  = ['https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4' , 'https://www.sample-videos.com/video321/mp4/720/big_buck_bunny_720p_5mb.mp4']
data = download_videos(videos )



# Download a text file 
url = 'https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js'
file_name , text = download_static_code_file(url)
file_name

# For more info use the help function to read the docstrings
