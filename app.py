from flask import Flask, render_template, request
from automate import initBoard, definePinOut, writeToPort

initBoard()
definePinOut(7)
definePinOut(11)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')
    
@app.route('/', methods=['POST'])
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
    app.run(debug=True, host='0.0.0.0')