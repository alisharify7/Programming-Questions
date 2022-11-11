import sys

try:
    m = float(input('Enter Your Height in Meter: '))
    kg = float(input('Enter Weight in Kilogram: '))
except ValueError:
    print('Invalid input')
    sys.exit(0)

bmi = (kg / (m ** 2))
print(f'Your BMI is {bmi}')

if bmi < 18.5:
    print('Underweight')
elif(bmi >= 18.5 and bmi <= 24.9):
    print('Normal weight')
elif (bmi >= 25.0 and bmi <= 29.9):
    print('Obesity - Class One')
elif (bmi >= 30.0 and bmi <= 34.9):
    print('Obesity - Class Two')
elif (bmi >= 35.0 and bmi <= 39.9):
    print('Obesity - Class Three')
elif (bmi >= 40.0):
    print('Obesity - Class Four')
    