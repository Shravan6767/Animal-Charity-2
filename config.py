from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# create database
db = client["animal_charity"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]