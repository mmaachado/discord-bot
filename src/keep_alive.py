from threading import Thread

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'flask server online'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run, daemon=True).start()
