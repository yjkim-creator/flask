import pymongo
from pymongo import MongoClient

from pymongo import MongoClient
client = MongoClient("mongodb://test:1234@127.0.0.1:27017/")
db = client.mydb
rows = db.person.find()
for row in rows:
    print(row)

guestbook = db.guestbook
guestbook.insert({'id':1, 'title':'제목1','contents':'내용1', 'writer':'홍길동', 'wdate':'2019-03-15', 'age':23});
guestbook.insert({'id':2, 'title':'제목2','contents':'내용2', 'writer':'홍길동2', 'wdate':'2019-03-16', 'age':24});
guestbook.insert({'id':3, 'title':'제목3','contents':'내용3', 'writer':'홍길동3', 'wdate':'2019-03-17', 'age':25});
guestbook.insert({'id':4, 'title':'제목4','contents':'내용4', 'writer':'홍길동4', 'wdate':'2019-03-18', 'age':26});
guestbook.insert({'id':5, 'title':'제목5','contents':'내용5', 'writer':'홍길동5', 'wdate':'2019-03-19', 'age':27});

rows = db.guestbook.find()
for row in rows:
    print(row)

guestbook.remove({'id': '1'})

guestbook.update({'id':2}, {'$set':{'title': '제목을 수정합니다'}}, True)

rows = db.guestbook.find()
for row in rows:
    print(row)

print('조건 검색')
result2 = guestbook.find({'age':{'$gte':30}}) #크거나 같다
for r in result2:
    print(r)

#컬렉션 제거
guestbook.drop()

"""
콘솔에서는 복사 ctrl+enter 키
붙여넣기 마우스 오른쪽 버튼 누르기
"""