# def get_db():
#     from pymongo import MongoClient
#     client = MongoClient('localhost:27017')
#     db = client.tutDbs
#     return db

# def add_country(db):
#     db.countries.insert({"name" : "Canadacdf"})
    
# def get_country(db):
#     return db.post.find_one()

# if __name__ == "__main__":

#     db = get_db() 
#     add_country(db)
#     print get_country(db)
from pymongo import MongoClient
client = MongoClient()
db = client.test
cursor = db.restaurants.find({"restaurant_id" : "40361606"})
for document in cursor:
    print(document)