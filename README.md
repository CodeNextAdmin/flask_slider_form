# flask_slider_form
A simple example of using an HTML range slider to send values to a Flask server with no JavaScript using a form submit. This file is a starter challenge.
Used for Google's Code Next **Team Edge Web** course. 
### Term 1, Lab 3 Flask with Hardware

## Setup:
1. Clone the project to a Raspberry Pi.
2. Make sure you have installed [Python Flask](https://flask.palletsprojects.com/en/2.0.x/installation/). 
3. Fromt the Linux Terminal, cd into the directory you cloned the repo into. 
4. run app.py: `$ python app.py`. to launch the Flask server and go to the specified URL to open in a client browser.
5. Test that the slider works when you click "Submit". 

## Challenge
1. Connect your Pi to a Servo using following a pinout example from [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/recipes.html#servo).
2. In `app.py`, complete the POST method function that receives the value from the HTML slider so it moves the servo to the desired angle, only between 0-180 degrees.
3. Make sure to import the necessary libraries.
4. Test and debug.
