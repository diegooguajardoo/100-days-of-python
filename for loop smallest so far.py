#look for the smallest so far

smallest = None
print ("before")
for value in [9, 41,12,3,74,15]:
	if smallest == None:
		smallest = value
	elif value < smallest:
		smallest = value
	print(smallest, value)

print("After", smallest)