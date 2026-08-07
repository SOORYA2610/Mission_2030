print("=" * 40)
print("WELCOME TO MISSION 2030")
print("=" * 40)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dream = input("What is your dream career? ")
study = int(input("How many hours do you study every day? "))

print("\n----- PROFILE -----")
print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"Dream : {dream}")
print(f"Study : {study * 7}")

years = 25 - age

if years > 0:
    print(f"\nYou have about {years} years until you're 25.")
else:
    print("\nKeep learning and improving every day!")

