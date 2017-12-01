from flask import Flask, render_template
app = Flask(__name__)


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



@app.route('/restaurants/')
@app.route('/')
def showAllRestaurants():
	output = "This page displays all restaurants"
	return render_template('restaurants.html', restaurants = restaurants)

@app.route('/<int:restaurant_id>/menu')
def showAllMenuItems(restaurant_id):
	output = "This page displays all menu items for a given restaurant"
	return output

@app.route('/add_restaurant')
def addRestaurant():
	output = "Here you can add a new restaurant"
	return output

@app.route('/<int:restaurant_id>/edit_restaurant')
def editRestaurant(restaurant_id):
	output = "Here you can edit a restaurants name"
	return output	

@app.route('/<int:restaurant_id>/delete_restaurant')
def deleteRestaurant(restaurant_id):
	output = "Here you will be asked if you are shure you want to delete a given restaurant"
	return output	

@app.route('/<int:restaurant_id>/menu/add_menu_item')
def addMenuItem(restaurant_id):
	output = "Here you can add e new menu item"
	return output	

@app.route('/<int:restaurant_id>/menu/<int:item_id>/edit_menu_item')
def editMenuItem(restaurant_id, item_id):
	output = "Here you can edit a menu item"
	return output		

@app.route('/<int:restaurant_id>/menu/<int:item_id>/delete_menu_item')
def deleteMenuItem(restaurant_id, item_id):
	output = "Here you will be asked if you are shure you want to delete a given menu item"
	return output	

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)