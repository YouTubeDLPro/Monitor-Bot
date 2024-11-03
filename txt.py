import requests
import time
from flask import Flask
import threading

PORT = "YOUR_PORT_HERE"

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

# Function to run the Flask app
def run_flask():
    app.run(host='0.0.0.0', port=PORT)

# Function to check the bot's status
def check_bot_status():
    url = "YOUR_URL_HERE"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Bot is up!")
            else:
                print(f"Bot returned status code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred: {e}")

        time.sleep(5)  # Wait for 5 seconds before the next check

# Start the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Start checking the bot status
check_bot_status()
