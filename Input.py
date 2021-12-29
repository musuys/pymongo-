##데이터 넣기
from pymongo import MongoClient
client= MongoClient('localhost', 27017)
db= client.test1

db.users.insert_one({'id': 11, 'name': '스파이더맨', 'age': 19})
db.users.insert_one({'id': 22, 'name': '아이언맨', 'age': 40})
db.users.insert_one({'id': 33, 'name': '토르', 'age': 100})
db.users.insert_one({'id': 44, 'name': '닥터스트레인지', 'age': 40})
db.users.insert_one({'id': 55, 'name': '헐크', 'age' : 45})
