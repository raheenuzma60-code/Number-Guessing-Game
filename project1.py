import random

print("Choose Difficulty Level")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    max_number = 50
elif choice == 2:
    max_number = 100
elif choice == 3:
    max_number = 500
else:
    print("Invalid choice! Defaulting to Medium level.")
    max_number = 100

comp = random.randint(1, max_number)

user = 0
attempts = 0

while user != comp:
    user = int(input(f"Guess a number between 1 and {max_number}: "))
    attempts += 1

    if user == comp:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
    elif user < comp:
        print("📉 Too low! Try a higher number.")
    else:
        print("📈 Too high! Try a lower number.")