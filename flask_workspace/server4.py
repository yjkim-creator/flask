#세션, get방식, post 방식 전송에 대한 이야기

from flask import Flask, render_template
from flask import request, session

app = Flask(__name__)
"""
정보를 전송하는 방식
클라이언트(브라우저)로부터 서버로 정보를 전송하는 방식
header 요소를 먼저 보내고, 나중에 body 를 따로 보낸다.
1.GET - header만 보낸다. 간단하고 길이도 짧고 보안을 요하지 않는 정보
    HTTP://127.0.0.1:5000/user?name=Tom&age=23&email=test@hanmail.net
    name 이라는 키값으로 Tom
    age라는 키값으로 23
    email = test@hanmail.net
2.POST
    우선 header 에 간단한 정보 보내고
    body 부분에 실제 정보 + 파일같은거 보낼때 
    외부에 정보가 안드러나고 한글도 안깨진다. 보낼 수 있는 정보의 양에 제한이 없다.

정보를 저장하기
각 페이지와 페이지는 정보를 저장하지 못한다
웹페이지는 하나의 페이지로부터 다른페이지로 값을 공유할수 없다.
쿠기 
    - 사용자 컴퓨터에 텍스트파일의 형태로 정보가 저장된다
    - 보안문제 때문에 거의 안쓴다.
    - 온라인 강의 진도체크 이런정보만 쿠키에 넣는다
세션
    - 서버에 저장된다.
    - 로긴정보, 장바구니 정보등 비교적 간단하고 짧은 정보만
    - 너무 많은 저옵를 저장하면 서버가 벅차한다. 더많은 정보는 데이터베이스에
    저장해놓고 필요할때마다 불러쓴다.
    - 각 클라이언트마다 새로운 세션객체가 하나씩 만들어진다
    - 파이썬은 대부분 dict 타입이다.
    session["userid"]="test
    userid = session["userid"]
"""

app.secret_Key="45j23jkl4jkl"

@app.route("/", methods=['POST', 'GET'])
def index():
    return "<h1>Welcome</h1>"

@app.route("/loginForm")
def loginForm():
    return render_template("/loginForm.html")

@app.route("/login", methods=['POST'])
def login():
    userid = request.form['userid'] #POST방식으로 데이터를 보낼때 처리하기
    passwd = request.form['passwd']
    if userid=="test" and passwd=="1234":        
        session['logFlag']=True
        session['userid']=userid
        msg="로긴성공 {}".format(userid)
    else:
        msg="로긴실패"
    return msg

@app.route("/user", methods=['GET'])
def getUser():
    if session.get('logFlag')!=True:
        return "잘못된 접근입니다."
    userid=session['userid']
    return "userid : {0}".format(userid)


if __name__=="__main__":
    app.debug = True
    app.run()
