
import mysql.connector

mydb = mysql.connector.connect(host='outran.in',user='outratnh_esp_board',password='password',database='outratnh_esp_data',)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)