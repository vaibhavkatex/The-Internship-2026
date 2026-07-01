
# Create a class Student with attributes name and marks.
class Student:

    # Add a method calculate_grade() that returns "Pass" if marks ≥ 40, otherwise Fail
    def __init__(self,name,marks):
      self.name =name
      self.marks =marks

    def calculate_grade(self):
       if self.marks >= 40:
        return "Pass"
       else:
        return "Fail"
       
# Create 3 student objects, display their details, andprint their grades.
Student1 = Student ("Vaibhav" , 89)
Student2 = Student ("Ram" , 91)
Student3 = Student ("Rahual" , 28)


print("\nStudent Name :", Student1.name,"\nStudent Marks :" ,Student1.marks,"\nStudent Grade:",Student1.calculate_grade())
print("\nStudent Name :", Student2.name,"\nStudent Marks :" ,Student2.marks,"\nStudent Grade:",Student2.calculate_grade())
print("\nStudent Name :", Student3.name,"\nStudent Marks :" ,Student3.marks,"\nStudent Grade:",Student3.calculate_grade()) 