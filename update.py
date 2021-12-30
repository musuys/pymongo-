from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test1

#name이 스파이더맨인 항목 모두를 블랙위도우로 바꾸고 id값 1111로 변경
db.users.update_many({"name" : "스파이더맨"}, {"$set" : {"id" : "1111", "name" : "블랙위도우"}})


all_users = list(db.users.find({}))

for user in all_users:
    print(user)