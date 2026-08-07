print("=" * 40)
print("WELCOME TO MISSION 2030")
print("=" * 40)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dream = input("What is your dream career? ")
study_hours = int(input("How many hours do you study every day? "))
weekly_hours = study_hours * 7

print("\n----- PROFILE -----")
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"Dream          : {dream}")
print(f"Study per week : {weekly_hours} hours")

years = 25 - age

if years > 0:
    print(f"\nYou have about {years} years until you're 25.")
else:
    print("\nKeep learning and improving every day!")

