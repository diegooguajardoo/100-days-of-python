import random
def master():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)
  next = rnd1 +1 
  

  print(rnd1 +1)
  print(quotes[rnd1])
  print(next +1)
  print(quotes[next])
  print("also this")
  print(rnd2)
  print(quotes[rnd2])
if __name__== "__master__":
  master()
