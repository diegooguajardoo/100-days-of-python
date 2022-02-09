import random
champion = 0
cont = "yes"
tries = 0
while True: 
	cont = input("Do you want to continue?\n").lower()
	tries +=1
	if cont == "y" or cont == "yes":
		participant = (random.randint(1,80))
		if int(participant) > champion:
			if tries  > 2:
				print("WIN!")
				print("Former champion: ", champion, "Beated by new Champion: ", participant)
			elif tries == 1:
				print("Initial champion: ", participant)
			champion = participant
		elif participant == champion:
			print("TIE")
			print("participant", participant, "is equal to current champion.")
		else:
			print("LOSE")
			print ("participant", participant, " is not greater than", champion)
	else:
		break
print("After", tries, "tries...")
print("The champion number is: ", champion)
