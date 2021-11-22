from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define routes for the HTML page

# tells Flask what to display when we're looking at the home page, index.html
@app.route("/")
#define function
def index():
   
   #uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script 
   mars = mongo.db.mars.find_one()
   
    #tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.
    #tells Python to use the "mars" collection in MongoDB
   return render_template("index.html", mars=mars)


#The next lines allow us to access the database, scrape new data using our scraping.py
@app.route("/scrape")

# Define it with def scrape():
def scrape():

    #we assign a new variable that points to our Mongo database
   mars = mongo.db.mars

   #created a new variable to hold the newly scraped data
   mars_data = scraping.scrape_all()
   
   # with the gathered new data, we need to update the database using .update()
   #upsert=True. This indicates to Mongo to create a new document if one doesn't already exist, and new data will always be saved (even if we haven't already created a document for it).
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
    app.run()