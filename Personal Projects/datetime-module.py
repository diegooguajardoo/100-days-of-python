import time
from datetime import datetime


#datetime(year, month, day)
#a1 es el primer artista
b1 = datetime(2022,4, 2,8,15)


def imprimirhora():
	seconds = time.time()
	local_time = time.ctime(seconds)
	print("Hora actual:", local_time)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("Ya es hora de: Artista")

#countdown()
imprimirhora()
#print(b1)

