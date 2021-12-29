from pymongo import MongoClient
#특정데이터만 가져오기
client =MongoClient('localhost', 27017)
db=client.test1

all_users = list(db.users.find({'id':22}))

for user in all_users:
    print(user)