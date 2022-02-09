
usrinp = input("Do you want a list?: ")
if usrinp != "y":
	quit() 

# while loop know the stoping conditions
#while number > 0:
#	number = number - 1
#	print(number)


import random
definition = input("random or defined list?: ").lower()

if definition == "random":
	maxnumb = int(input("Type any your maximum number:"))
	randrange = random.randint(0,maxnumb)
	for i in range(0, randrange): #random number of iterations
		print(i)

elif definition == "defined":
	definitiontop = int(input("Type the maximum number of your list: "))
	#for i in [0,1,2,3,4,5,6,7,8]: #defined number of iterations
	for i in range(0,(definitiontop +1)):
		print(i)
else:
	print("There\'s only two options of list availiable")

print("Here's your", definition, "list.")
