fruit = input("Type any word:")
last = len(fruit)
while last > 0:
	print(fruit[last-1])
	last = last - 1
	if last == 0: #si index (o sea variable "last") es cero, significa que es la primera letra
		break
print("Done")
