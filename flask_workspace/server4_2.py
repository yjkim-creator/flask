#청사진(blueprint)를 이용해서 라우터를 분리하자

from flask import Flask, Blueprint, request, session, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Blue Print 테스트"

#라우터를 여러개의 파일로 나누기
#import 구문을 썼을때 경로지정안하면 같은 폴더에 있는 파일을 불러온다
import test
import board
#Flask객체에 등록하기
app.register_blueprint(test.bp)
app.register_blueprint(board.bp)

if __name__=="__main__":
    app.debug=True
    app.run()