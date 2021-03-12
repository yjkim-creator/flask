

#pip install pymysql 
import pymysql

#접속객체를 가져온다. 
conn = pymysql.connect( host = 'localhost',  #서버아이피
                         user = 'root',    #계정아이디
                         password = '1111' , #패스워드
                         db = 'mydb',        #db명
                         port=3306)          #디비포트번호 
curs = conn.cursor()

sql = """
     insert into guestbook(title, contents, writer, wdate)
     values(%s, %s, %s, now())
"""
curs.execute(sql, ('제목6', '내용6', '작성자6')) # 쿼리문 실행 - 실행후 fetch하기 
conn.commit()

sql = "select * from guestbook"
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute(sql)

rows = curs.fetchall() # 데이터 패치- tuple타입으로 온다 

for row in rows :
     print(row['title'], row['contents'], row['writer'], row['wdate'])
conn.close()



