#connection to the mangodb
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db=client["user-Details"]    #Creation of the database
collection=db["name and mail"]