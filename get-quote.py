import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd = random.randint(0, last)
  next = rnd +1 

  print(rnd +1)
  print(quotes[rnd])
  
  print(next +1)
  print(quotes[next])
  

if __name__== "__main__":
  main()
