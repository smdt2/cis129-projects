#Sebastian Melendez
#CIS129


with open('grades.txt', 'w') as file:
    # Enter grades 
    while True:
        grade = input("Enter a grade (or 'quit' to stop): ")
        if grade.lower() == 'quit':
            break
        # Write the grade to the file
        file.write(grade + '\n')


with open('grades.txt', 'r') as file:
    # Read all lines from the file
    grades = file.readlines()

# Convert grades to integers
grades = [int(grade.strip()) for grade in grades]

# Display individual grades
print("Individual Grades:")
for grade in grades:
    print(grade)

# Calculate total, count, and average
total = sum(grades)
count = len(grades)
average = total / count

# Display total, count, and average
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")

import csv


with open('grades.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])

    # Enter student records
    while True:
        firstname = input("Enter student's first name (or 'quit' to stop): ")
        if firstname.lower() == 'quit':
            break
        lastname = input("Enter student's last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))

        # Write the student record to the CSV file
        writer.writerow([firstname, lastname, exam1, exam2, exam3])
