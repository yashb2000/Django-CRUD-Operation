import pymysql

class EmpOperations:
    def checkuser(self,id,ps):
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from users where userid='%s' and psw='%s'" %(id,ps))
        data=curs.fetchone()
        if data:
            page="Admin.html"
        else:
            page="Failure.html"
        con.close()
        return page
    
    