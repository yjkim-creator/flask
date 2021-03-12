import pymongo
from pymongo import MongoClient

from pymongo import MongoClient
client = MongoClient("mongodb://test:1234@127.0.0.1:27017/")
db = client.mydb
rows = db.person.find()
for row in rows:
    print(row)


"""
콘솔에서는 복사 ctrl+enter 키
붙여넣기 마우스 오른쪽 버튼 누르기
"""