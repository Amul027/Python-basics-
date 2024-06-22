import sqlite3
conn=sqlite3.connect("customerdata.db")

cur=conn.cursor()
cur.execute("create table mydata(name varchar(50),roll_no varchar(50),password varchar(340))")
cur.execute('insert into mydata values("ramu","501","ramanji123")')
cur.execute('insert into mydata values("shekar","554","shekar123")')
cur.execute('insert into mydata values("amul","527","amul123")')
x=cur.execute('select * from mydata')
print(x.fetchall())
conn.commit()
 