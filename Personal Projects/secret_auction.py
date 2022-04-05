biders = dict()

def addbider(name, quant):
	biders[name] = quant

while True:
	bider = input("What is your name: \n")
	if bider != "exit":
		amount = int(input("How much would you want to put? \n"))
		addbider(bider, amount)
		clear()
	else:
		break

print(biders)
maxbid = 0
for i in biders:
	if biders[i] > maxbid:
		maxbid = biders[i]
		winner = i
print(winner, maxbid)
