import time
import serial
ser = serial.Serial('COM8', 9600,timeout=None) # Establish the connection on a specific port
time.sleep(2)
fwd="FFRBBlDFBLLRfbLRd"
#fwd="RRRRRRRRRRRRRRRRRRRRRRR"
def shuffle():
    
    for char in fwd:
        ser.write(char.encode())
        time.sleep(1)
bwd=fwd.swapcase()[::-1]
print(bwd)

def revshuffle():
    for char in bwd:
        ser.write(char.encode())
        time.sleep(1)
#shuffle()
#time.sleep(10)
revshuffle()
