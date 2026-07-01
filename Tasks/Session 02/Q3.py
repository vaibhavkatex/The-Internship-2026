# Q3.py - Grade calculator based on marks

# Take student marks as input
marks = int(input("Enter your marks: "))

# Check marks against grading scale
if marks >= 90:
    print("Grade A - Excellent")
elif marks >= 75:
    print("Grade B - Good")
elif marks >= 60:
    print("Grade C - Average")
elif marks >= 40:
    print("Grade D - Pass")
else:
    print("Fail")
