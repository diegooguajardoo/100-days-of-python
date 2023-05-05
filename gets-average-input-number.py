cnt = 0
total = 0
average = 0

while True:
	number = input("Enter a number: ")
	if number == "done":
		break
	try:
		number = int(number)
	except:
		print("Invalid input")
		continue
	cnt = cnt + 1
	total = number + total
	average = total / cnt

print(total, cnt, average)