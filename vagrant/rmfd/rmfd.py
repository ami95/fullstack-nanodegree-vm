from flask import Flask 
app = Flask(__name__)


@app.route('/')
@app.route('/login')
def renderLoginPage():
	output = "This page displays the login form"
	return output

@app.route('/sign_up')
def renderSignUpPage():
	output = "This page displays the sign-up form"
	return output

@app.route('/my_profile')
def renderMyProfile():
	output = "This page displays the logged in users profile"
	return output

@app.route('/search')
def filterSearch():
	output = "On this site you can search a new roommate, using filter criteria"
	return output

@app.route('/user/<int:user_id>')
def renderUserProfile(user_id):
	output = "On this site you can check another users profile"
	return output

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)