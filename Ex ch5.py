cnt = 0
total = 0
average = 0

while True:
	number = input("Enter a number: ")
	if number == "done":
		print("Total is: ",total)
		print("Count is: ",cnt)
		print("Average is: ",average)
		break
	try:
		number = int(number)
	except:
		print("Invalid input")
		continue
	cnt = cnt + 1
	total = number + total
	average = total / cnt
