from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<H1>Hello, Python!!</H1>"

@app.route("/hello")
def hello():
    return "<span style='color:#00ff00:font-size:20pt'>Hello. Python!!</span>"

@app.route("/hello2")
def hello2():
    temp = "Python 은 배우기 쉬운언어입니다<br/>"
    temp = temp + "아주 재미있습니다<br/>"
    return temp

@app.route("/user/<username>")
def userinfo(username):
    temp = username + "님 환영합니다"
    return temp

@app.route("/user/<username>/<age>")
def userinfo2(username, age):
    temp = username + "님 나이는" + age + "입니다"
    return temp

@app.route("/page/<page>/key/<key>")
def pageinfor(page, key):
    temp = page + "" + key
    return temp

@app.route("/calc/<num1>/<num2>/<key>")
def pagecalc(num1, num2, key):
    if key == "1":
        temp = int(num1) + int(num2)
        temp = f"{num1} + {num2}={temp}"
    elif key == "2":
        temp = int(num1) - int(num2)
        temp = f"{num1} - {num2}={temp}"
    elif key == "3":
        temp = int(num1) * int(num2)
        temp = f"{num1} * {num2}={temp}"
    elif key == "4": 
        temp = int(num1) // int(num2)
        temp = f"{num1} / {num2}={temp}"
    temp = str(temp) + "입니다"
    return temp


if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=5000)
