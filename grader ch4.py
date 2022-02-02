def compute(sc):
	try:
		float(sc) or sc >1 #si es numero o mas de 1
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
			print ("Your grade is:", grade)
			return grade
	except:
		print("Bad score") #todo tipo de bad score


score = input("What is the score? \n")
total = compute(score)
