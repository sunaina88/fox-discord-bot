from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return "🦊 Fox Bot is alive! Visit /uptime for status."

@app.route('/uptime')
def uptime():
    return f"Bot uptime: {time.time()}"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    print("Keep-alive server started on port 8080.")
