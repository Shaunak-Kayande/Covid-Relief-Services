import mysql.connector as connector

class UserInfo:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists user(name VARCHAR(20), age INT, mobile VARCHAR(12), username VARCHAR(20) PRIMARY KEY, password VARCHAR(20) )'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    #Insert
    def insert_user(self, name, age, mobile, username, password):
        query= "INSERT INTO user values('{}', {}, '{}', '{}', '{}')".format(name, age, mobile, username, password)
        self.cur.execute(query)
        self.con.commit()
    
    #Checking username and password
    def checkUsername(self, username, password):
        query= "SELECT * FROM user WHERE username='{}' AND password='{}'".format(username, password)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        if not rows:
            return 0
        else: return 1
        


# user = UserInfo()
# print(user.checkUsername("shaun", "shaun"))