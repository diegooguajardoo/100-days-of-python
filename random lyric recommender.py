password = "cheat"

import random

def lyrics(song):
	if song == 1:
		print("\"'Hooray, hooray, I was your silver lining. Hooray, hooray, but now I\'m gold.\"")
	elif song == 2:
		print("\"Touch me! It's so easy to leave me all alone with the memory of my days in the sun.\"")
	elif song == 3:
		print("\"I'm not their hero, but that doesn't mean that I wasn't brave\"")
	elif song == 4:
		print("\"Everything passes. Everything changes. Just do what you think you should do\"")
	else:
		print(song)

valid = input("Do you want a random song line? Y/N\n")


if valid == "Y" or valid == "y":
	t = [1,2,3,4]
	x = random.choice(t)
	x = int(x)
	try:
		lyrics (x)
		print("Good, that was song number",x)
	except:
		quit()
	
elif valid == password:
	lyrics("haz encontrado el santo grial")

else:
	print("Thanks,come back later.")

