def compute(sc):
	if sc <= 1:
		if sc >= .9:
			grade = "A"
		elif sc >=.8:
			grade = "B"
		elif sc >=.7:
			grade = "C"
		elif sc >=.6:
			grade = "D"
		elif sc <.6:
			grade = "F"
		return grade
	else:
		print("Type a number between 0 and 1 please")


score = input("What is the score? \n")

try:
	score = float(score)
	total = compute(score)
	print ("Your grade is:", total)
except:
	print("Enter a digit please")
	
