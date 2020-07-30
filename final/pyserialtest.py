import time
import serial
ser = serial.Serial('COM7', 9600,timeout=None) # Establish the connection on a specific port
time.sleep(2)
#sol="RLFFBBrlDDRLFFBBrlLLRLFFBBrlDRLFFBBrldfRLFFBBrlDDRLFFBBrlRLRLFFBBrlDRLFFBBrlFLBBRRDBBRLFFBBrlDRLFFBBrlFFRLFFBBrlDRLFFBBrlRRBBDD"
#sol=sol[::-1].swapcase()
#for i in sol[::-1]:
#    ser.write(i.encode())
##for i in range(60):
##    print("start"+str(i))
##    ser.write('F'.encode())
##    print(ser.isOpen())
##    print("end"+str(i))
##time.sleep(30)
ser.write('R'.encode())
ser.write('L'.encode())
for i in range(60):
    print("start"+str(i))
    ser.write('D'.encode())
    time.sleep(1)
    ser.write('D'.encode())
    time.sleep(1)
    ser.write('F'.encode())
##    print(ser.isOpen())
##    print("end"+str(i))
##print("done")
##time.sleep(1)
##for i in range(10):
##    ser.write('F'.encode())
##time.sleep(30)
##for i in range(10):
##    ser.write('R'.encode())
##print("done")
##time.sleep(1)
##
##
##ser.write('R'.encode())
##time.sleep(1)
##
##ser.write('F'.encode())
##time.sleep(1)
##ser.write('B'.encode())
