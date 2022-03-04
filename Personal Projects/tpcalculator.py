print("Welcome to the tip calculator")
subtotal = float(input("What was the total bill? "))
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = int(input("How many poeple wil pay the bill? "))

percentageth = float("1." + percentage)
total = round(subtotal * percentageth / people)
print(f"Each person should pay: ${total}")