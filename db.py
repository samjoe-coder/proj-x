import random
from pymongo import MongoClient

# Replace with your actual MongoDB Atlas URI
MONGO_URI = "mongodb+srv://system:123samMonGODB@project-x.d6nm8yo.mongodb.net/?retryWrites=true&w=majority&appName=project-x"

client = MongoClient(MONGO_URI)
db = client["dropdown_db"]
collection = db["items"]

categories = [
    "Electronics", "Furniture", "Books", "Clothing", "Sports",
    "Toys", "Groceries", "Tools", "Vehicles", "Music"
]

collection.delete_many({})  # Clear existing data

# Generate 1,000 items per category
bulk_data = []
for category in categories:
    for i in range(1000):
        item_name = f"{category}_Item_{i+1}"
        bulk_data.append({
            "category": category,
            "item": item_name
        })

# Bulk insert
collection.insert_many(bulk_data)

print(f"Inserted {len(bulk_data)} documents.")
