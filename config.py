from pymongo import MongoClient
import os

# connect to 
client = MongoClient(os.environ.get("MONGO_URI"))

# create database
db = client["animal_charity_2"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]
