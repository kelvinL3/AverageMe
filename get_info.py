import os
# import smth
import averager

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
	for root, dirs, files in os.walk("static/average"):
		for file in files:
			# print os.path.join(root, file)
			# print file
			averages.append(os.path.join(root, file))
	average = averages[0]
	for avg in averages:
		if ".png" in avg:
			average = avg
	return average

def create_result():
	arr = ["static/all_images/", "static/average/average.png"]
	averager.averager(averager.list_imgpaths(arr[0]), out_filename=arr[1])
	return
