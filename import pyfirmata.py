#alle importene for at scriptet skal fungere
import time
from Adafruit_IO import Client, Feed, RequestError
import pyfirmata


#nøkkelen til adafruit dashboardet til min bruker
ADAFRUIT_IO_USERNAME = "stian4223"
ADAFRUIT_IO_KEY = "aio_ewpD44MV3WTwLqMAJtaW26QpwZvW"

#Lager en klient som komuniserer med arduinoen
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#starter opp pyfirmata komunikasjon med arduino
board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
digital_output = board.get_pin('d:10:o')

#her seier vi at koden skal sende og taimot signal fra adafruit 
try:
    lys = aio.feeds('lys')
    potentiometer = aio.feeds('potentiometer')
except RequestError:
    feed = Feed(name='lys')
    feed2 = Feed(name='potentiometer')
    lys = aio.create_feed(feed)
    potentiometer = aio.create_feed(feed2)

while True:
    data = aio.receive(lys.key)
    data2 = aio.send(potentiometer.key, analog_input.read())

    if data.value == "ON":
        digital_output.write(True)
    if data.value == "OFF":
        digital_output.write(False)
    time.sleep(3)
