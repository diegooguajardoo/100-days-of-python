latestmax = 0
for thing in [9,41,12,3,74,15]:
	if thing > latestmax:
		latestmax = thing
		print(latestmax,thing)
	else:
		print (thing, "not greater than", latestmax)
 
print("done")
