print("Welcome to the Tip Calculator.\n")
bill = float(input("What was the total bill?\n"))
people = float(input("\nHow many people to split the bill?\n"))
tip_percent = float(input("\nWhat percentage tip would you like to give?\n")) / 100
tip_amount = bill * tip_percent
split = (bill + tip_amount) / people
print(f"\nEach person should pay: ${split:.2f}\n")