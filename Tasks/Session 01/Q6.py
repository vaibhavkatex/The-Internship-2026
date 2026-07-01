# S1Q6.py - BMI Calculator

print("--- BMI Calculator ---")

# Inputs converted to float for decimal values
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

# BMI formula
bmi = weight / (height ** 2)

print(f"\nYour BMI is: {round(bmi, 2)}")
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
else:
    print("Category: Overweight")
