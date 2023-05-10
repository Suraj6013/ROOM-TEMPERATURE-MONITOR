from flask import Flask, render_template,url_for
import requests
import threading
import time

app = Flask(__name__)

def get_data():
    api_url = 'http://192.168.213.36'
    response = requests.get(api_url)
    data = response.json()
    temperature = data.get('Temperature')
    humidity = data.get('Humidity')
    return temperature, humidity

@app.route('/')
def index():
    temperature, humidity = get_data()
    return render_template('index.html', temperature=temperature, humidity=humidity)

@app.before_request
def activate_job():
    if not hasattr(app, 'temperature'):
        def update_data():
            while True:
                temperature, humidity = get_data()
                time.sleep(1)
                app.temperature = temperature
                app.humidity = humidity
        thread = threading.Thread(target=update_data)
        thread.start()

@app.context_processor
def inject_values():
    return {'temperature': getattr(app, 'temperature', None), 'humidity': getattr(app, 'humidity', None)}

if __name__ == '__main__':
    app.run()
