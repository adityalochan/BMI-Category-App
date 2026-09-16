print('Welcome to BMI calculator app')

# BMI Formula: weight/height**2

height = float(input("Enter your height in meters | Range 0-2.72 -- "))
weight = float(input("Enter your weight | Range 1-700 -- "))

bmi = height/weight**2

print("Your BMI is {}".format(bmi))
