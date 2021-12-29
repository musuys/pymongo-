from pymongo import MongoClient
#모든 데이터 가져오기
client = MongoClient('localhost', 27017)
db=client.test1

all_users = list(db.users.find({}))

for user in all_users:
    print(user)