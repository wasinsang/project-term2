import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('com4', 9600)
command = input("Type something..: (on/ off / bye )");
if command =="on":
	print ("The LED is on...")
	time.sleep(5)
	arduino.write(b'H')
elif command =="off":
	print ("The LED is off...")
	time.sleep(5)
	arduino.write(b'L')
elif command =="bye":
	print ("See You!...")
	time.sleep(5)
	arduino.close()
else:
	print ("Sorry..type another thing..!")
