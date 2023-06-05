import serial
import qrcode
from PIL import Image

# Connect to the Arduino via the serial port
arduino = serial.Serial('/dev/cu.usbmodem101', 9600)

# Wait for Arduino to be ready
while not arduino.readline().strip().decode() == "READY":
    pass

# Generate the QR code
qr_data = "Hello, Arduino!"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)

# Convert the QR code to a PIL Image object
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image = qr_image.convert("1")

# Resize the image to match the printer's width
width, height = qr_image.size
printer_width = 384  # Adjust the width based on your thermal printer
scale_factor = printer_width / width
new_size = (int(width * scale_factor), int(height * scale_factor))
qr_image = qr_image.resize(new_size)

# Convert the image to a byte array
qr_bytearray = qr_image.tobytes()

# Send the QR code data to the Arduino
arduino.write(qr_bytearray)
arduino.write(b'\n')

# Close the serial connection
arduino.close()
