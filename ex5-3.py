largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
	elif num > largest:
		largest = num


print("Maximum", largest)