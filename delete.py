from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db=client.test1

db.users.delete_many({'id' : 44})

all_users = list(db.users.find({}))
for user in all_users:
    print(user)