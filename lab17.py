from flask import Flask, render_template

# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def hello():
	return 'Hello world from Flask!'
@app.route('/home')
def home():
	return render_template('home.html')
#@app.route('/julian')
#def julian():
#	return render_template('template.html')
if __name__ == '__main__':
	app.run(debug=True)