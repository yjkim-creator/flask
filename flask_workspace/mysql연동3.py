

#pip install pymysql 
import pymysql

#접속객체를 가져온다. 
conn = pymysql.connect( host = 'localhost',  #서버아이피
                         user = 'root',    #계정아이디
                         password = '1111' , #패스워드
                         db = 'mydb',        #db명
                         port=3306)          #디비포트번호 

curs = conn.cursor(pymysql.cursors.DictCursor)

def insert():
     title = input("제목 : ")
     writer = input("작성자 : ")
     contents = input("내용 : ")
     sql = """
          insert into guestbook(title, contents, writer, wdate)
          values (%s, %s, %s, now())
     """
     curs.execute(sql, (title, writer, contents))
     conn.commit()

def update():
     id = input("수정할 아이디는?")
     title = input("수정할 제목 : ")
     writer = input("수정할 작성자 : ")
     contents = input("수정할 내용 : ")

     sql = """update guestbook
               set title = %s, contents=%s, writer=%s
               where id=%s
          """
     curs.execute(sql, (title, contents, writer, id))
     conn.commit()

def delete():
     id= input("삭제할 아이디는 : ")

     sql = "delete from guestbook where id =%s"
     curs.execute(sql, id)

def output():
     sql = "SELECT * FROM guestbook"
     curs.execute(sql)

     rows = curs.fetchall()

     for row in rows:
          print(row['id'], row['title'], row['writer'], row['contents'], row['wdate'])

def end():
     conn.close()

while(True):
     sel = input("1.목록 2.추가 3.수정 4.삭제 0.종료 :")
     if sel =="1":
          output()
     elif sel == "2":
          insert()
     elif sel == "3":
          update()
     elif sel == "4":
          delete()
     elif sel == "0":
          break
          

     
