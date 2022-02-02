def computepay(aliash, aliasr):
	if aliash <= 40:
		pay = aliash * aliasr
		print(pay)
	else:
		extrahrs = aliash - 40
		regpay = 40 * aliasr
		extrapay = extrahrs * aliasr * 1.5
		pay = regpay + extrapay
		print(pay)
	return pay	

floathrs = float(input("Enter hours: "))
floatregularrate = float(input("Enter rate: "))

p = computepay(floathrs, floatregularrate)
#pay = hrs * regularrate



    #if extrahrs > 1:
    #    print("you got payed",extrahrs,"extra hours!")
    #else:
    #    print("you got payed",extrahrs,"extra hour!")
    