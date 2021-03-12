#filename : serverBoard.py

from flask import Flask, request, session, render_template 
from flask import redirect, url_for
import DBModule


app = Flask(__name__)

db = DBModule.Database()

@app.route("/")
def index():
    return render_template("/index2.html")

@app.route("/board/list")
def board_list():
    dataList = db.executeAll("select * from guestbook")
    return render_template("/board2/board_list.html",  dataList=dataList)
 
#/board/view/1
@app.route("/board/view/<int:id>")
def board_view(id):
    sql = "select * from guestbook where id=%s"
    data = db.executeOne(sql, (id))
    return render_template("/board2/board_view.html",  data = data)

@app.route("/board/write")
def board_write():
    data = dict()
    data['title'] = ""
    data['writer'] = ""
    data['contents'] = ""
    data['wdate'] = ""
    data['id'] = ""
    return render_template("/board2/board_write.html",data = data, mode="insert")

@app.route("/board/save", methods=['POST'])
def board_save():    
    title = request.form['title']
    contents = request.form['contents']
    writer = request.form['writer']
    sql ="""
        insert into guestbook(title, contents, writer, wdate)
        values(%s, %s, %s, now())
    """
    db.execute(sql, (title, contents, writer))
    return redirect("/board/list") #새로운 url로 이동한다 

"""
@app.route("/board/delete")
def board_delete():
    id = request.values['id']
    sql = ""
        delete from guestbook where id =%s
    ""
    db.execute(sql, (id))
    return redirect("/board/list")
"""

@app.route("/board/delete/<int:id>")
def board_delete(id):        
    sql = "delete from guestbook where id =%s"
    data = db.execute(sql, (id))
    return redirect("/board/list")

@app.route("/board/modify/<int:id>")
def board_modify(id):
    sql = "select * from guestbook where id=%s"
    data = db.executeOne(sql, (id))

    return render_template("/board2/board_write.html", data= data, mode="modify")

@app.route("/board/update", methods=["POST"])
def board_update():
    id = request.form['id']
    title = request.form['title']
    contents = request.form['contents']
    writer = request.form['writer']
    sql = """
        update guestbook set title =%s, writer=%s, contents=%s 
        where id=%s
    """
    db.execute(sql, (title, writer, contents, id))

    return redirect("/board/list")


if __name__ == "__main__":
    app.debug=True
    app.run() 
