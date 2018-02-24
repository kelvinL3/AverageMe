from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/average')
def average():
	return render_template('home.html', images=images, average=average)

if __name__ == '__main__':
	app.run(debug=True)