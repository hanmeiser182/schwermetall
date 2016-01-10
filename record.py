import sys, os
import platform

try:
    import serial  # Python2
except ImportError:
    from serial3 import *  # Python3



print(platform.python_version())
print(os.getcwd())

def do_record(number_of_records=20):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    target = open("out.csv", 'w')
    count=0
    ser.flushInput()
    while count < number_of_records:
        count = count + 1
        text = ser.readline()
        print text
        print count
        if (len(text.split(",")) == 4):
            target.write(text)
    target.close()
    ser.close()


def go():
    do_record()