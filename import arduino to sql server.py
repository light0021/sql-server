#alle import filene vi trenger for å kjøre koden
import datetime
import pyfirmata
import mysql.connector
import time

#her setter vi inn all informasjonen til der man finner serveren som kor den er hostet eller passordet.
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

#gjer inputen om til ein string
analog_input = board.get_pin('a:0:i')

#setter vi heile greia i ein loop sån vi slepper å kjøre koden pånytt kvar gong
while True:
    print ("connected..")

    #gjer at stringen blir om til ein variabel(den har ein verdi)
    analog_value = analog_input.read()

    #seier kva som skal bli gjort in til sql
    sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

    verdi = analog_value
    tid = datetime.datetime.now()

    val = (verdi,tid)

    print("Executing...")

    mycursor.execute(sql, val)
    mydb.commit()

    print ("Done")
    time.sleep(4)
