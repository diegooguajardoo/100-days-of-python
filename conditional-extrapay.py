workedhours = input("How many hours did you worked?")
workedhours = int(workedhours)

regularrate = 10
extrarate = 15
if workedhours <= 40:
    pay = workedhours * regularrate
    print(pay)
else:
    extrahrs = workedhours - 40
    pay = 40 * regularrate
    extrapay = extrahrs * extrarate
    pay = pay + extrapay
    print(pay)
    if extrahrs > 1:
        print("you got payed",extrahrs,"extra hours!")
    else:
        print("you got payed",extrahrs,"extra hour!")
    