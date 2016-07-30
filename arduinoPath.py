from arduinoCommands import *
import serial
import time

class ArduinoPath:
    def __init__(self,path):
        commands = Commands(path).commands
        arduino = serial.Serial("COM9", 9600)
        time.sleep(2)
        arduino.write(commands.encode('ascii'))
        arduino.close()
