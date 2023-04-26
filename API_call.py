from pymongo import MongoClient

client = MongoClient('mongodb+srv://varunusar:root@cluster0.9q7alis.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("Project")
records= db.Users
print(records.find_one({"username":"hello;"}))
