#html 문서를 일일이 다 수작업으로 못하니까
#html 파일을 렌더링 
#html 파일을 templates 라는 폴더에 넣어놓고 서비스한다.
#css/javascript/image 는 static 폴더에 넣도록 설정되어 있다

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def user():
    return render_template("user.html",
        title="사용자정보",
        name="홍길동",
        age="23",
        mylist=[1,2,3,4,5])
#list of dict : 표기형식이 JSON 형태
dataList = [
    {'title':'쌍갑포차', 'author': '배혜수', 'price':'8000'},
    {'title':'신과함께', 'author': '주호민', 'price':'12000'},
    {'title':'아지갑놓고나왔다', 'author': '미역', 'price':'8000'},
    {'title':'해리포터와 마법사의돌', 'author': '조안롤링', 'price':'12000'},
    {'title':'관촌수필', 'author': '이문구', 'price':'16000'},
]

@app.route("/book")
def book():
    return render_template("book.html", book= dataList )


if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=5000)
