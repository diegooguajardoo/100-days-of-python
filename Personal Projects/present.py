import datetime

present = datetime.datetime.now()

claxons = datetime.datetime(2022, 4, 2, 17, 45)
gepe = datetime.datetime(2022, 4, 2, 18, 25)
caribou = datetime.datetime(2022, 4, 2, 19, 35)
clubz = datetime.datetime(2022, 4, 2, 19, 40)
parcels = datetime.datetime(2022, 4, 2, 20, 15)
bizarrap = datetime.datetime(2022, 4, 2, 20, 40)
guayna = datetime.datetime(2022, 4, 2, 23, 15)
strokes = datetime.datetime(2022, 4, 3, 0, 0)


differencestrokes = strokes - present
differenceparcels = parcels - present
differenceguayna = guayna - present
differencecaribou = caribou - present
differenceclubz = clubz - present
differencegepe = gepe - present
differenceclaxons = claxons - present
differencebizarrap = bizarrap - present


print(f"Now: {present}")

print(f"Claxons in {differenceclaxons}")
print(f"Gepe in {differencegepe}")
print(f"Caribou in {differencecaribou}")
print(f"Cluubz in {differenceclubz}")
print(f"Parcels in {differenceparcels}")
print(f"Bizarrap in {differencebizarrap}")
print(f"Guayna in {differenceguayna}")
print(f"Strokes in {differencestrokes}")

