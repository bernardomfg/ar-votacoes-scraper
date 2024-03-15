# modules/database.py
import mongoengine as mongo

def connect_to_database(connectionString):
    mongo.connect(host=connectionString)