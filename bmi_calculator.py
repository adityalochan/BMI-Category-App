print('Welcome to BMI calculator app')

# BMI Formula: weight/height**2

height = float(input("Enter your height in meters | Range 0-2.72 -- "))
weight = float(input("Enter your weight | Range 1-700 -- "))



bmi = height/weight**2

# bmi < 18.5 : Under Weight
# bmi < 25 : Normal Weight
# bmi < 30 : Over Weight
# bmi >30  : Obese

condition = 'Unknown'

if bmi<18.5:
    condition = 'Under Weight'
elif bmi < 25:
    condition = 'Normal Weight'
elif bmi < 30:
    condition = 'Over Weight'
else:
    condition = 'Obese'

print("Your BMI is {}. You are {}".format(bmi,condition))
