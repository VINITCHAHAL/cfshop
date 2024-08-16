from django.shortcuts import render , redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
import gridfs
from django.core.files.storage import default_storage
from bson import ObjectId


def home(request):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["coffeeshop"]
    shop = db["shop"]

    # Retrieve all documents (or use a query to filter)
    documents = shop.find()

    # Prepare data for the template
    items = [{
        'name': doc.get("name", "Name not found"),
        'price': doc.get("price", "Price not found"),
        'quantity': doc.get("quantity", "Quantity not found"),
        'image_url': doc.get("image")  # Use the URL directly
    } for doc in documents]

    context = {
        'items': items
    }

    return render(request, 'home.html', context)




