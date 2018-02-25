from flask import Flask, render_template, request
import get_info
import main
import random
# import main as pyimgur

app = Flask(__name__)

@app.route('/')
def index():
	images = get_info.get_all_images()
	return render_template('home.html', images=images)

@app.route('/average', methods=["POST", "GET"])
def average():
	# main()
	main.main()
	get_info.create_result()
	images = get_info.get_all_images()
	average = get_info.get_average() + "?" + `random.random()`;
	return render_template('average.html', images=images, average=average)

if __name__ == '__main__':
	app.run(debug=True)
