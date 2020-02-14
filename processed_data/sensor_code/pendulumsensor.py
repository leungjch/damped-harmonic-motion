import serial
import time
import csv

ser = serial.Serial('COM8')
ser.flushInput()
startTime = time.time()
while True:

    ser_bytes = ser.readline()
    decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    print(decoded_bytes)
    with open("data.csv","a", ) as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time.time()-startTime,decoded_bytes])
