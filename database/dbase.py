import sqlite3
con=sqlite3.connect("dbbase.db")
# try:
#     con.execute("create table user(no int,name text,age int)")
# except:
#     print("table created")    
    
# con.execute("insert into user(no,name,age)values(1,'tom',20),(2,'tim',21),(3,'hari',24),(4,'akhil',13),(5,'karthik',11)")
# con.commit()

# data=con.execute("select * from user where name like '%u'")
# data=con.execute("select * from user where name like '____'")
                                                                              
# data=con.execute("select *from user order by name")
# data=con.execute(select * from user order by name desc)
# for i in data:
#     print(i)

# try:
#     con.execute("create table address(no int,place text,pin int)")
# except:
#     print("table created")  
    
# con.execute("insert into address(no,place,pin)values(1,'ekm',680720),(2,'tsr',680521),(4,'tvm',680532)")
# con.commit()

# data=con.execute("select user.no,user.name,user.age,address.place,address.pin from user inner join address on user.no=address.no")
# data=con.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no")
# data=con.execute("select user.no,user.name,user.age,address.place,address.pin from address  left join user on user.no=address.no")

# for i in data:
#     print(i)

# data=con.execute("select name,count(age) from user group by name")
# data=con.execute("select name,min(age) from user group by name")
# data=con.execute("select name,max(age) from user group by name")
# data=con.execute("select name,avg(age) from user group by name")
data=con.execute("select name,sum(age) from user group by name")


for i in data:
    print (i)