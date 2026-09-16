# BMI Category Reporter

A simple Python command-line program that calculates a user's Body Mass Index (BMI) using their height and weight and reports the corresponding BMI category.

## Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run
Run the program using:
python bmi_calculator.py

## Example

Enter your height in meters : 1.75
Enter your weight in kilograms : 70
Your BMI is 22.86. Your BMI category is Normal weight.


## Known limitations
- The program requires height to be entered in meters and weight in kilograms.
- The program does not currently support imperial units. 
- The program might break for edge cases like null etc