from flask import Flask, jsonify, render_template, request
import serial
import serial.tools.list_ports

### serial stuff ###
def connectToArduino():
    arduino_ports = [
        port.device for port in serial.tools.list_ports.grep(r"Arduino")
    ]

    if arduino_ports:
        portname = arduino_ports[0]
        ser = serial.Serial(portname, 9600)
        print("Connected to Arduino port: " + portname)
        return ser
    else:
        print("No Arduino boards found. Please connect an Arduino board and try again.")
        return None

ser = connectToArduino()

def sendToArduino(text):
    if (ser != None):
        ser.write(text.encode())
        print("Sent following to arduino: " + text)

        recvd_from_arduino = b""
        while ser.read() != b"\r":
            recvd_from_arduino += ser.read()

        print(recvd_from_arduino.decode())
    else:
        print("not connected to arduino")
### end of serial stuff ###

### flask stuff ###

app = Flask(__name__)

@app.route("/send", methods=['POST'])
def text():
    data = request.json
    print(data["secret"])
    sendToArduino(data["secret"])
    return jsonify({
        "response": "recieved request"
    })

@app.route('/')
def index():
    return render_template('index.html')

### flask stuff ### 