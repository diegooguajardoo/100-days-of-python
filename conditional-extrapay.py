hrs = input("Enter hours: ")
regularrate = input("Enter rate: ")
try:
    hrs = float(hrs)
    regularrate = float(regularrate)
except:
    print("Enter valid number")
quit()

extrarate = regularrate * 1.5
if hrs <= 40:
    pay = hrs * regularrate
    print(pay)
else:
    extrahrs = hrs - 40
    pay = 40 * regularrate
    extrapay = extrahrs * extrarate
    pay = pay + extrapay
    print(pay)
    #if extrahrs > 1:
    #    print("you got payed",extrahrs,"extra hours!")
    #else:
    #    print("you got payed",extrahrs,"extra hour!")
    