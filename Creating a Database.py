import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database = "demo")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
mycursor.execute("select * from student")
result = mycursor.fetchone()
for i in result:
  print(i)
print(result)
