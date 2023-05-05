inp = input("How old are you?")
try:
	typeinp = int(inp)
	print("Nice work")
except:
	typeinp = 1
	print("Try again with a digit")