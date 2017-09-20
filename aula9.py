import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)
i = 0

while i < 100:
   temperatura = ser.readline().decode('utf-8')
   temperatura = temperatura.strip('\n')
   
   hora = datetime.now().strftime('%H:%M:%S')
   str = '{};{};{}'.format(i, hora, temperatura)
   print(str)
   i += 1
