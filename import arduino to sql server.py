import datetime
import pyfirmata
import mysql.connector
import time


mydb = mysql.connector.connect(
host="localhost",
user="root",
password="elevelev",
database="fil logging"
)
mycursor = mydb.cursor()

#starter opp pyfirmata komunikasjon med arduino
board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()
analog_input = board.get_pin('a:0:i')

while True:
    print ("connected..")


    analog_value = analog_input.read()

    sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

    verdi = analog_value
    tid = datetime.datetime.now()

    val = (verdi,tid)

    print("Executing...")

    mycursor.execute(sql, val)
    mydb.commit()

    print ("Done")
    time.sleep(4)
