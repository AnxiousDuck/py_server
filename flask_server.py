from flask import Flask, jsonify, render_template, request
import serial
import serial.tools.list_ports
import requests

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

        pastebin_link = post_to_pastebin(text)

        unique_part = pastebin_link.split('/')[3]

        ser.write(unique_part.encode())
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


### morse code stuff ###

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    morse_text = []
    for char in text.upper():
        if char in morse_code:
            morse_text.append(morse_code[char])
    return ' '.join(morse_text)

# Example usage
text = "HELLO WORLD"
morse_text = text_to_morse(text)
print(morse_text)

### morse stuff ###


### send to pastebin and return link stuff ###


# Function to post text to Pastebin
def post_to_pastebin(text):
    url = "https://pastebin.com/api/api_post.php"
    params = {
        "api_dev_key": "sKkskSBiaYhH4-WBUQUWHJRDw7chcS__",
        "api_option": "paste",
        "api_paste_code": text
    }
    response = requests.post(url, data=params)
    return response.text.strip()

# Function to shorten a URL using is.gd

def shorten_url(url):
    api_url = "https://is.gd/create.php"
    params = {"format": "json", "url": url}
    response = requests.get(api_url, params=params)
    return response.json()["shorturl"]

# Example usage
# text = "This is some example text."
# pastebin_link = post_to_pastebin(text)
# short_pastebin_link = shorten_url(pastebin_link)
# print("Pastebin Link:", pastebin_link)
# print("Shortened Pastebin Link:", short_pastebin_link)