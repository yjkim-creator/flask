#filename : serverBoard.py

from flask import Flask, request, session, render_template 
from flask import redirect, url_for

app = Flask(__name__)

#파이썬 list of dict  dict타입객체들을 list에 담은건데 
#json 의 객체 저장방식과 동일 
dataList = [
    {'id':'1', 'title':'제목1', 'contents':'내용1',   'writer':'홍길동1'},
    {'id':'2', 'title':'제목2', 'contents':'내용2',   'writer':'홍길동2'},
    {'id':'3', 'title':'제목3', 'contents':'내용3',   'writer':'홍길동3'},
]

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/board/list")
def board_list():
    return render_template("/board/board_list.html",  dataList=dataList)
 
#/board/view/1
@app.route("/board/view/<int:id>")
def board_view(id):
    return render_template("/board/board_view.html",  data = dataList[id-1])

@app.route("/board/write")
def board_write():
    return render_template("/board/board_write.html")

@app.route("/board/save", methods=['POST'])
def board_save():
    data = dict() #새로운 dict타입 객체를 만들고 
    data['id'] = len(dataList)+1  #id 자동증가 
    data['title'] = request.form['title']
    data['contents'] = request.form['contents']
    data['writer'] = request.form['writer']
    
    dataList.append( data ) #데이터에 추가 
    return redirect("/board/list") #새로운 url로 이동한다 


if __name__ == "__main__":
    app.debug=True
    app.run() 
