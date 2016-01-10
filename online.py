try:
    import serial  # Python2
except ImportError:
    from serial3 import *  # Python3

from nupic.frameworks.opf.modelfactory import ModelFactory

import os,sys

ser = serial.Serial('/dev/ttyACM0', 9600)

def get_online(number_of_records=20):# 0 means forever
    model = ModelFactory.loadFromCheckpoint(os.getcwd() + "/model_save")

    count=0
    ser.flushInput()
    while (count < number_of_records) or (number_of_records == 0):
        count = count + 1
        text = ser.readline()
        if (len(text.split(",")) == 4):
            result = model.run({
                "s1": float(text.split(",")[0]),
                "s2": float(text.split(",")[1]),
                "s3": float(text.split(",")[2]),
                "s4": float(text.split(",")[3])
            })
            prediction = int(result.inferences['multiStepBestPredictions'][4])
            sys.stdout.write("\r"+ str(prediction))
            sys.stdout.write("\t"+ text)
            ser.write(str(prediction)+ '\n')