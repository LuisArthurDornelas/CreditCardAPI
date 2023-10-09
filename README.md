# Credit Card Validation

## Description
This projects consists in a Credit Card Validation app, it checks:
- Expiry Data
Not allowing invalid months and past dates (ex: 45/25 or 02/20).
- Validity of credit card number (PAN)
Uses Luhn's algorithm to do so, read more about it at [here](https://en.wikipedia.org/wiki/Luhn_algorithm).
- CVV length 
Where America Express Cards (which PAN starts with either "34" or "37") need to have 4 digits, and the other cards only 3.
- Blank fields
Additionally, it prevents the user from submitting the form if any of the fields are left empty.

## Prerequisites
To run this project, you'll need:
- Python (can be downloaded [here](https://www.python.org/downloads/))
- Flask (can be obtained by typing `pip install flask` on the terminal once Python is installed)

## Setup
With Flask and Python installed, the program can be executed through the following command:
`python app.py`

With the program running, enter your browser and go to `http://127.0.0.1:5000/validate` to acces the form and start testing the tool.