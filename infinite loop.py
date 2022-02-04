import random

print("Select difficulty level: easy, medium, hard")
difficulty = input("How hard do you want the level to be?")

difficulty.lower() == ["easy", "medium", "hard"]
if difficulty == "easy":
	top_of_range = 10
elif difficulty == "medium":
	top_of_range = 30
else:
	top_of_range = 100

random_number = random.randint(0, top_of_range)
guesses = 0
print ("Random number is", random_number)
while True:
	user_guess = int(input("Make a guess"))
	guesses += 1
	if user_guess == random_number:
		print("Right!")
		break
	elif user_guess > top_of_range:
		print("Make it smaller")
	else:
		print("Make it higher, take note of the difficulty")
	continue

print("you got it in", guesses, "guesses")
