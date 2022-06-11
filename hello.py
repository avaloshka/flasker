from flask import Flask, render_template

# create flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')
def home():
	first_name = 'Alex'
	stuff = 'This is <bold>my stuff</bold>!'
	favorite_pizza = ['Pepperoni', 'Mushrooms', 'Four cheese', 'Tomato']
	return render_template('home.html',
	 first_name=first_name,
	  stuff=stuff,
	  favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

# Create custom error pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

