import requests
import time
from flask import Flask
import threading

# Configuration variables
FLASK_PORT = 10000           # Port for Flask to run on Render
BOT_URL = "http://t.me/seagame_top_up_bot/start"  # Replace with actual bot status URL if available
CHECK_INTERVAL = 5           # Time interval in seconds for checking bot status

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running with Gunicorn!"

# Function to check the bot's status in a loop
def check_bot_status():
    while True:
        try:
            # Ping the bot URL
            response = requests.get(BOT_URL)
            if response.status_code == 200:
                print("Bot is up!")
            else:
                print(f"Bot returned status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

        time.sleep(CHECK_INTERVAL)  # Wait for the next check

# Start the bot status check in a background thread
def start_checking_bot_status():
    bot_thread = threading.Thread(target=check_bot_status)
    bot_thread.daemon = True  # Daemonize thread to ensure it closes with main program
    bot_thread.start()

# Initialize the bot status check thread
start_checking_bot_status()

# Gunicorn will import and run 'app', so we don’t call app.run directly here
