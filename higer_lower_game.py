import 
from game_data import data
import random
def rd():
  return random.randint(0,50)
  

person1 = data[rd()]
name1 = person1["name"]
description1 = person1["description"]
country1 = person1["country"]
followers1 = person1["follower_count"]

person2 = data[rd()]
name2 = person2["name"]
description2 = person2["description"]
country2 = person2["country"]
followers2 = person2["follower_count"]


#resultados
print(f"Compare A: {name1}, a {description1} from {country1}")
print(f"Compare B: {name2}, a {description2} from {country2}")

#comput
def comp(p1,p2):
  if p1 > p2:
    return "A"
  elif p2 > p1:
    return "B"

correct = comp(followers1, followers2)
    
#question
answer = input("Who has more followers? Type 'A' or 'B': ")

if answer.upper() == correct:
  print("Right!")
else:
  print("Wrong!")

  