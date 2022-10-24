import mysql.connector
import datetime
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="elevelev",
database="fil logging"
)
mycursor = mydb.cursor()

print("Connected..")

sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

verdi = 1.0 # Verdi som blir skrevet til databasen(sensor - verdi(float))

tid = datetime.datetime.now() # Tid som blir skrevet til databasen(sensor - tid (datetime))

val = (verdi, tid)

print("Executing...")

mycursor.execute(sql, val)
mydb.commit()

print("done")
