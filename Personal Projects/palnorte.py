import time
from replit import clear

def refresh():
	seconds = time.time()
	local_time = time.ctime(seconds)
	print("Local time:", local_time)


while input("Refresh?") == "ok":
	
	refresh()
	clear()
