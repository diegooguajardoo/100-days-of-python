print ("Welcome to Diego\'s game")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
	quit()

score = 0

answer = input("What is the capital of Italy?\n")
if answer.lower() == "rome":
	print("correct!")
	score +=1

answer = input("What is the capital of Mexico?\n")
if answer.lower() == "mexico city":
	print ("correct!")
	score +=1

answer = input("What is the capital of France?\n")
if answer.lower() == "paris":
	print ("correct!")
	score +=1

answer = input("What is the capital of Russia?\n")
if answer.lower() == "moscow":
	print ("correct!")
	score +=1

print("You\'ve ended the game")
print ("You\'ve scored " + str(score) + " points")

percent = float(score)/4
if score >= .75:
	print("Contratulations you have passed the test")
else:
	print ("You\'ve failed, try again.")