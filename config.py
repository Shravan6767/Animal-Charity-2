from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://shravan67:Gokuandvegeta16@cluster0.qf0m9y0.mongodb.net/?appName=Cluster0")

# create database
db = client["animal_charity_2"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]
