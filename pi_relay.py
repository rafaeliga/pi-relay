from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import sys

def initBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def definePinOut(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)

def writeToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)

initBoard()
definePinOut(7)
definePinOut(11)

application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return render_template('form.html')
    
@application.route('/', methods=['POST'])
def submit():
    command = request.form['command']
    print(command)
    
    if(command == '1ON'):
        writeToPort(7,0)
    
    if(command == '1OFF'):
        writeToPort(7,1)
    
    if(command == '2ON'):
        writeToPort(11,0)
    
    if(command == '2OFF'):
        writeToPort(11,1)
        
    return render_template('form.html')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
