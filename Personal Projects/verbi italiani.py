verbo = input("Aggiungere un verbo regolare al infinito per favore: ")
coniu = ["are", "ere", "ire"]
if verbo[- 3] == "a":
	coniu = "-are"
elif verbo[- 3] == "i":
	coniu = "-ire"
else:
	coniu = "-ere"

print(verbo)
print(coniu)
print("Radice: ", verbo[0:(len(verbo)-3)])
for desinenze in ["o","i","a","iamo","ate","ono"]:
	print(verbo[0:(len(verbo)-3)] + desinenze)

