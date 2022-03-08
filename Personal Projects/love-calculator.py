# 🚨 Don't change the code below 👇
from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
couple = name1 + name2
true = "true"
love = "love"
total_true = 0
total_love = 0

#print(f"For {name1}.")
for letters in true:
	counts = couple.count(letters)
	total_true = counts + total_true
	print(f"{letters} occurs {counts} times.")
for letters in love:
	counts = couple.count(letters)
	total_love = counts + total_love
	print(f"{letters} occurs {counts} times.")

#this block redoes a for loop for separate names print(f"For {name2}.")
#for letters in true:
#	counts = name2.count(letters)
#	total_true = counts + total_true
#	print(f"{letters} occurs {counts} times.")
#for letters in love:
#	counts = name2.count(letters)
#	total_love = counts + total_love
#	print(f"{letters} occurs {counts} times.")

print(f"Your love score is {total_true}{total_love} %.")


