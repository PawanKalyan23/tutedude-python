student_grades = {}

# Add a new student
name = input("Enter student name: ")
grade = input("Enter grade: ")

student_grades[name] = grade

# Update an existing student's grade
update_name = input("Enter student name to update: ")

if update_name in student_grades:
    new_grade = input("Enter new grade: ")
    student_grades[update_name] = new_grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

# Print all student grades
print("\nStudent Grades:")

for student, grade in student_grades.items():
    print(student, ":", grade)