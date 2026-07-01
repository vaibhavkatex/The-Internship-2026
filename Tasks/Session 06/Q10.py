# Q10. (Mini Project - Combined Concepts)

# Take student details
name = input("Enter Student Name: ")
roll_no = input("Enter Student Roll No: ")

# Create empty list for marks
marks = []

# Take 5 subject marks as input
for i in range(5):
    mark = float(input(f"Enter Subject {i+1} Marks: "))
    marks.append(mark)

# Print marks list
print("\nMarks List:", marks)

# Add one more subject mark using append()
extra_mark = float(input("Enter one more subject mark: "))
marks.append(extra_mark)

print("\nUpdated Marks List:", marks)

# Print highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Sort marks in descending order
marks.sort(reverse=True)
print("Marks in Descending Order:", marks)

# Calculate average marks
average = sum(marks) / len(marks)
print("Average Marks:", average)

# Show total number of subjects
print("Total Number of Subjects:", len(marks))