import random

print("Select difficulty level: easy, medium, hard")
difficulty = input("How hard do you want the level to be?\n")

difficulty.lower() == ["easy", "medium", "hard"]
if difficulty == "easy":
	top_of_range = 10
elif difficulty == "medium":
	top_of_range = 30
else:
	top_of_range = 100

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
	guesses += 1
	user_guess = input("Make a guess: ")
	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("Please type a number next time)")
		continue #this takes the user to the top of the loop if it is not a digit, therefore asking again for a digit guess

	if user_guess == random_number:
		print("Right!")
		break
	else:
		print("you got it wrong!")
#	elif user_guess > top_of_range:
#		print("Make it smaller\n")
#	else:
#		print("Make it higher\n")
#	continue	
#

print("you got it in", guesses, "guesses")
print(random_number)
