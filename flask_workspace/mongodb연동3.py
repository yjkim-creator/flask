import pymongo
from pymongo import MongoClient

from pymongo import MongoClient
client = MongoClient("mongodb://test:1234@127.0.0.1:27017/")
db = client.mydb

guestbook = db.guestbook

def get_sequence(name):
    document = db.customSequence.find_one_and_update({"_id":"guestbook"},
                {"$inc": {"seq":1}}, return_document=True)
    return document['seq']

id = str(get_sequence('guestbook'))
guestbook.insert_one({'id':id, 'title':'제목'+id, 'contents':'내용'+id, 'writer':'홍길동'+id, 'wdate':'2021-02-23','age':23})

rows= db.guestbook.find()
for row in rows:
    print(row)