import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player = int(
	input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer = random.randint(0, 2)

if player >= 3 or player < 0:
	print("You typed an invalid number.")
elif player + 2 == computer:
	result = "Player wins"
elif computer + 2 == player:
  result = "Computer wins"
elif player > computer:
	result = "Player wins"
elif player == computer:
  result = "Tie"
else:
	result = "Computer wins "

hand = [rock, paper, scissors]
print(f"Player: {hand[player]}")
print(f"Computer: {hand[computer]}")

print(f"Result: {result}")
