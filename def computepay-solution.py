def computepay(h, r):
	
	if h > 40:
		pay = (40 * r) + r * 1.5 * (h-40)
	else:
		pay = h * r
	return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

pay = computepay(hrs, rate)
print("Pay:", pay)