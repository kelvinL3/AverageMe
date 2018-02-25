import os

def get_all_images():
	images = []
	for root, dirs, files in os.walk("static/all_images"):
		for file in files:
			#print os.path.join(root, file)
			#print file
			images.append(os.path.join(root, file))
	return images

def get_average():
	averages = []
	for root, dirs, files in os.walk("static/all_images"):
		for file in files:
			#print os.path.join(root, file)
			#print file
			averages.append(os.path.join(root, file))
	average = averages[0]
	return average