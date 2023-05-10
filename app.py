from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time
import time

from random import random
from flask import Flask, render_template, make_response
import serial

app = Flask(__name__)
ser = serial.Serial('COM10', 115200)

if ser.isOpen==False:
    ser.open()
temp = []

    
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


while True:
    read = ser.readline().decode().rstrip()
    temp = read.split()
    time.sleep(10) 

    
@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    Temperature = temp[0]
    Humidity = temp[1]

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response
# ser.close()
if __name__ == "__main__":
    app.run(debug=True)
