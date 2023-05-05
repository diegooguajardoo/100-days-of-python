import random

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
game_active = True
number = random.randint(0,100)

if difficulty == "easy":
	attempts = 10
elif difficulty == "hard":
	attempts = 5
else:
	print("Please select valid level")
	quit()

def match(reference, user_try):
	if user_try == reference:
		print("You're are correct")
		return True
	elif user_try > reference:
		print("Too high")
		return False
	elif user_try < reference:
		print("Too low")
		return False

while game_active == True:
	attempts -=1
	guess = int(input("Make a guess: "))
	if match(number,guess):
		game_active = False
	elif attempts <= 0:
		game_active = False
	else:
		print("Guess again.")
		print(f"You have {attempts} remaining to guess the number.")