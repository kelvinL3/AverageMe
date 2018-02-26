# CLIENT_ID = "005be7347063d3e"
# im = pyimgur.Imgur(CLIENT_ID)
# image = im.get_image('S1jmapR')
# print(image.title) # Cat Ying & Yang
# print(image.link) # http://imgur.com/S1jmapR.jpg

import pyimgur
import webbrowser
import config


INPUT_ALBUM_ID = "55HpT"
OUTPUT_ALBUM_ID = "BV2Rd"

def connect_to_imgur():
	PATH = 'res.jpg'

	im = pyimgur.Imgur(config.CLIENT_ID, config.CLIENT_SECRET)
	auth_url = im.authorization_url('pin')
	webbrowser.open(auth_url)
	pin = raw_input("What is the pin? ")
	x = im.exchange_pin(pin)
	print(x)
	return im

def create_album(im, name):
	im.create_album(title=name)

def download_pictures(im, album_id):
	input_album = im.get_album(album_id)
	images = input_album.images
	return images

def upload_picture(im, path, album_id):
	uploaded_image = im.upload_image(path, album=OUTPUT_ALBUM_ID)
	print(uploaded_image.title)
	print(uploaded_image.link)
	print(uploaded_image.size)
	print(uploaded_image.type)

def clear_folder(folder):
	import os, shutil
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception as e:
			print(e)

def main():
	# on button click
	im = connect_to_imgur()

	while True:
		ans = raw_input("Do Demo?")
		if ans is "y":
			images = download_pictures(im, INPUT_ALBUM_ID)
			# delete all images in the temp folder
			clear_folder("static/all_images")
			i = 0
			for img in images:
				img.download(path = "./static/all_images/", name=str(i))
				i+=1
			# process
			PATH = "static/average/average.png"
			upload_picture(im, PATH, OUTPUT_ALBUM_ID) # this method prints out to console
		return


# refresh every hour
# im.refresh_access_token()


# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
# print uploaded_image.link


# get an array of
