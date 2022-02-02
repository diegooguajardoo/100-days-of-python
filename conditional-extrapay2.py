def computepay(h, r):
	if h > 40:
		pay = (40 * r) + ((h - 40) * r * 1.5)
	else:
		pay = h * r
	return pay	

floathrs = float(input("Enter hours: "))
floatregularrate = float(input("Enter rate: "))

p = computepay(floathrs, floatregularrate)
print ("Pay", p)
#pay = hrs * regularrate



    #if extrahrs > 1:
    #    print("you got payed",extrahrs,"extra hours!")
    #else:
    #    print("you got payed",extrahrs,"extra hour!")
    