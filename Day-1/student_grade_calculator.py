# Day 1 -> Simple Student Grade Calculator

# Calculating Grade
def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else: 
        return "F"

# Get Student Details
name = input("Enter Student name: ")

# Read Marks
marks = []

for i in range(1,6):
    mark = int(input(f"Enter Subject {i} Marks: "))
    marks.append(mark)

# Calculate Total and Average
total = sum(marks)
average = total // len(marks)

grade = calculate_grade(average)

# Display Result 
print(" STUDENT RESULT ".center(40,"="))
print(f"Student Name  : {name}")
print(f"Student Marks : {marks}")
print(f"Total Marks   : {total}")
print(f"Average       : {average:.1f}")
print(f"Grade         : {grade}")
print("=" * 40)