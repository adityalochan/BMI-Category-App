# BMI Category Reporter

A simple Python command-line program that calculates a user's Body Mass Index (BMI) using their height and weight and reports the corresponding BMI category.

## Setup

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

macOS/Linux:
source .venv/bin/activate

Windows:
.venv\Scripts\activate

Install the requirements:

pip install -r requirements.txt

## Run

Run the program using:

python bmi_calculator.py

## Example

Enter your height in meters (for example, 1.75): 1.75
Enter your weight in kilograms (for example, 70): 70
Your BMI is 22.86. Your BMI category is Normal weight.

The program also validates user input. For example:

Enter your height in meters (for example, 1.75): 0
Invalid height. Height must be between 0 and 2.5 meters.

## Known limitations

- The program requires height to be entered in meters and weight in kilograms.
- The program does not currently support imperial units such as feet, inches, or pounds.
- The BMI categories are intended as a simple classification for this application and do not account for individual factors such as body composition.