from socket import *
import pymysql

sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("0.0.0.0",6000))

date,addr=sockfd.recvfrom(2048)
print("客户端IP",addr)
print(date.decode())

db1=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",database='五月你好',charset='utf8')
cur=db1.cursor()
cur.execute("insert into class (姓名,sex,age,score) values (%s,%s,%d,%d)")
cur.close()
db1.close()
