import pymysql

#변수를 생성하는 위치는 클래스에 해도 되고, 생성자에서 만들어도 된다.
#변수를 함수외부에 만들면, 이 변수는 클래스 변수가 된다.
#static 필요 없이 변수를 클래스에 선언하면 이게 클래스변수(공용변수가 된다.)

#객체 만들면 객체들이 클래스 변수를 공유한다. 객체에서 변수의 값을 바꾸면
#비로소 새로운 메모리 만들어서 객체 소유로 한다

#파이썬에서는 가급적 변수 선언은 생성자에서 하자
#클래스에 정의된 변수는 클래스 정의시에 딱 한번 만들어진다.
# 각 객체마다 별도의 변수를 만들고 싶으면 생성자에서 만들자
class Database:
    def __init__(self):
        self.db = pymysql.connect( host = 'localhost',  #서버아이피
                         user = 'root',    #계정아이디
                         password = '1111' , #패스워드
                         db = 'mydb',        #db명
                         port=3306)          #디비포트번호 
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)


    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        self.db.commit()

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
    
    def close(self):
        self.db.close()