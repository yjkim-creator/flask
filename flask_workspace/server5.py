from flask import Flask
from flask import request

app= Flask(__name__)

@app.route("/")
def index():
    return "<H1>Welcome flask!</H1>"

@app.route("/login", methods=['GET'])
def login_get():
    userid = request.values['userid']
    if "password" in request.values:
        password = request.values['password']
    else:
        password="없음"

    return "get 전송 : userid %s password %s " % (userid, password)

#post 방식 전송을 하려면 html 문서를 만들어서 form 태그의 method를 POST 로 주거나
#curl(리눅스, 윈도우 둘다가능, 콘솔)
#postman, insomnia (그래픽을 지원 사용 간편)
@app.route("/login", methods=['POST'])
def login_post():
    userid = request.values['userid']
    if "password" in request.values:
        password = request.values['password']
    else:
        password="없음"

    return "post 전송 : userid {0} password {1} " .format(userid, password)

if __name__=="__main__":
    app.debug=True
    app.run()