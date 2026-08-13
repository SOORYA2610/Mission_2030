marks = []

for i in range(5):
    while True:
        mark = int(input(f"Enter mark {i + 1}: "))

        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid mark! Enter a value between 0 and 100.")

print("\n----- RESULT -----")
print("Student Marks:")

for mark in marks:
    print(mark)

total = sum(marks)
print("Total:", total)

average = sum(marks) / len(marks)
print("Average:", average)

highest = max(marks)
lowest = min(marks)
print("Highest:", highest)
print("Lowest:", lowest)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade ="C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

if average >= 40:
    status = "PASS"
else:
    status = "FAIL"
print("Status:", status)