password = "cheat"

import random
from tkinter import Y


valid = input("Do you want a random song line? Y/N\n")

try: 
	valid = int(valid)
	times = valid
	valid = Y
except:
	pass

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

if valid == "Y" or valid == "y":
	t = [1,2,3,4]
	x = random.choice(t)
	x = int(x)
	try:

		lyrics (x)
		print("Good, that was song number",x)
		print("times", times)

	except:
		quit()
	
elif valid == password:
	lyrics("haz encontrado el santo grial")

else:
	print("Thanks,come back later.")

