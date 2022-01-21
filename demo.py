from serial import Serial
import time
import requests

arduino = Serial('COM3', 9600)
while True:
    time.sleep(2)
    cadena = arduino.readline()
    if cadena != "":
        response = requests.get('https://www.google.com')
        print(response)
    print(cadena)

arduino.close()