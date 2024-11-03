# Monitor Bot - Telegram Bot Status Checker with Flask

This project is a simple Python application that checks the status of a Telegram bot every few seconds while running a Flask web server. The web server shows that the program is up and running, and the bot checker lets you know if the bot is online.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Bot Status Checking**: Checks if the Telegram bot is accessible every few seconds.
- **Flask Web Server**: Runs a simple server that can be accessed in a browser to confirm the code is running.
- **Concurrency**: Both the bot status checker and the server run at the same time.

---

## Requirements

Make sure you have these installed:

1. **Python 3.x**: Download from [Python's official website](https://www.python.org/downloads/).
2. **Pip** (Python package installer): Comes with Python 3.x. You can check if it's installed by running:
   ```bash
   pip --version

3. Flask: Used for the web server.


4. Requests: Used for checking the bot status.




---

Installation

Step 1: Clone the Repository

1. Open a terminal (command prompt on Windows).


2. Type the following command and press Enter:

git clone https://github.com/YouTubeDLPro/Monitor-Bot.git


3. Go to the project directory:

cd Monitor-Bot



Step 2: Install the Required Packages

Install Flask and requests by running:

pip install Flask requests


---

Running the Application

1. Open the Code File:

Open the app.py file in any code editor (e.g., VS Code, PyCharm) or a text editor (e.g., Notepad).



2. Set the Bot URL:

Find the line in the code that says url = "YOUR_URL_HERE" and replace it with the URL of your Telegram bot. (You may need to configure your bot's start URL depending on your setup.)



3. Run the Application:

In your terminal, make sure you are still in the project folder.

Run the application by typing:

python app.py



4. Check the Flask Server:

Open a web browser and go to http://localhost:5000.

If everything is working, you should see a message saying "Flask server is running!"



5. Monitor the Bot Status:

In your terminal, you should see messages every 5 seconds telling you if the bot is up and running.

If there is an error, it will show up in the terminal.





---

Project Structure

app.py: The main script that runs the bot status checker and Flask server.



---

Troubleshooting

Port 5000 is in use: If you get an error about port 5000 being in use, try changing the port in the app.run(host='0.0.0.0', port=5000) line in app.py to another number, such as 5001, and restart the script.

Bot URL issues: If you don't see the expected messages in the terminal about the bot's status, check that you have the correct URL for your bot.

Packages not installed: If you get an error saying ModuleNotFoundError for Flask or requests, make sure to run pip install Flask requests again.



---

Contributing

Feel free to contribute! If you have ideas for improvements, submit an issue or a pull request.


---

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Author

Created by YouTubeDL. Happy coding!
