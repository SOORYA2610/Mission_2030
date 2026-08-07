print("=" * 40)
print("STUDENT GRADE ANALYZER")
print("=" * 40)

name = input("Enter student name: ")

marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 50:
    grade = "D"

else:
    grade = "FAIL"

if marks >= 35:
    status = "PASS"

else:
    status = "FAIL"

print("\n----- RESULT -----")

print("Name  :", name)
print("Marks :", marks)
print("Grade :", grade)
print("Status:", status)