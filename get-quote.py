import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd1 = random.randint(0, last)
  
  next = rnd1 +1 
  

  print(rnd1 +1)
  print(quotes[rnd1])
  print(next +1)
  print(quotes[next])
  
  
if __name__== "__main__":
  main()
