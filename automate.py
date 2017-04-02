import RPi.GPIO as GPIO
import sys

def initBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def definePinOut(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)
    
def writeToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)
