import mysql.connector
mydib=mysql.connector.connect(host="localhost",username="root",password="amuljadhav@2004")
mycursor=mydib.cursor()
#ycursor.execute("create database mydb")
mycursor.execute("show databases")
#mycursor.execute("create table cursor(name varchar(50),email varchar(50),password varchar(50)")
             #sql= insertinto(name,email,password,)values(%s,%s,%s)
print(mycursor)