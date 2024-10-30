import mysql.connector

con=mysql.connector.connect(host='localhost',user='pybatch',password='pybatch',database='batch2pm')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database batch2pm")
# cur.execute("create table user (no int,name text,age int)")
# cur.execute("insert into user (no,name,age) values(1,'saju',22)")
# cur.execute("insert into user (no,name,age) values(2,'akhil',23)")

# no=int(input("enter no"))
# name=input("name")
# # new_name=input("new_name")
# age=int(input("enter age"))
# cur.execute("insert into user (no,name,age) values(%s,%s,%s)",(no,name,age))

# # update
# cur.execute("update user set name=%s where name=%s ",(new_name,name))

# delete
# no=int(input('enter no'))
# cur.execute("delete from user where no=%s",(no,))



cur.execute("select * from user group by name")
data=cur.fetchall()
for i in data:
    print(i)




# cur.execute("select * from user where name like 'a%'")
# data=cur.fetchall()
# for i in data:
#     print(i)
