# -*- coding: utf-8 -*-
import serial, time

ser = serial.Serial('com3', 115200)
import struct


while 1:
    magic = ser.read()

    if magic != b'\xa5':
        print ("Bag magic number")
        continue
    data = ser.read(9)
    tagId = data[0].encode('hex')
    anchorId = data[1].encode('hex') 
    sequence = data[2].encode('hex')
    rssi = data[3].encode('hex')
    distance = (float)(struct.unpack('>I', data[4:8])[0]) / 100

    checksum = data[8]
    tagId = int(tagId, 16)
    anchorId = int(anchorId, 16) - 112
    rssi = int(rssi, 16)
    sequence = int(sequence, 16)

    print("%d %s %s %s %s" % (tagId, anchorId, distance, rssi, sequence))


    # time.sleep(1) # sleep 5 minutes

    # Loop restarts once the sleep is finished

ser.close() # Only executes once the loop exits