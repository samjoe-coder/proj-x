from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb+srv://system:123samMonGODB@project-x.d6nm8yo.mongodb.net/?retryWrites=true&w=majority&appName=project-x')
db = client["dropdown_db"]
categories_collection = db["categories"]

@app.route("/categories")
def get_categories():
    categories = db.items.distinct("category")
    return jsonify(categories)

@app.route("/items")
def get_items():
    category = request.args.get("category")
    items = db.items.find({"category": category}, {"item": 1, "_id": 0})
    item_list = [i["item"] for i in items]
    return jsonify(item_list)

if __name__ == "__main__":
    app.run(debug=True)
