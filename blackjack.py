#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	choice = random.choice(cards)
	return choice

def calculate_score(cards):
	if sum(cards) == 0 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)


def compare_score(user_score, computer_score):
	if user_score == computer_score:
		return "draw"
	elif computer_score == 0:
		return "Computer has blackjack"
	elif user_score == 0 and computer_score != 0:
		return "User has blackjack"
	elif user_score > 21:
		return "User loses"
	elif computer_score > 21:
		return "Computer loses"
	elif computer_score > user_score:
		return "Computer wins"
	elif user_score > computer_score:
		return "You Win!"
	else:
		return "you lose"

def play_game():
	computer_cards = []
	user_cards = []
	is_game_over = False

	for i in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"   Your have: {user_score} {user_cards}")
		print(f"   Computer has: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_should_deal = input("Do you want another card? Enter Y or N:\n")
			if user_should_deal.lower() == "y":
				user_cards.append(deal_card())
			else:
				is_game_over = True

	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)
	print(f"   Your final hand: {user_cards}, final score: {user_score}")
	print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #clear()
	play_game()


#def deal():
#	for i in range(0,2):
#		choice = random.choice(cards)
#		user_list.append(choice)
#	for i in range(0,2):
#		choice = random.choice(cards)
#		computer_list.append(choice)
#def current_winner():
#	if sum(computer_list) == 21:
#		print("Computer has blackjack!")
#		return "computer"
#		exit()
#
#	if sum(user_list) == 21:
#		print("User has blackjack!")
#		if current_winner == "computer":
#			return "draw"
#		else:
#			return "user"
#			exit()
#
#	if sum(user_list) > 21:
#		return "computer"
#
#	if sum(user_list) > sum(computer_list):
#		return "user"
#	elif sum(user_list) == sum(computer_list):
#		return "draw"
#	else:
#		return "computer"
#
#def results(win):
#	print(f"Winner is {win}")  
#	print(f"Computer had {sum(computer_list)} {computer_list}")
#	print(f"User had {sum(user_list)} {user_list}")
#
#deal()
#game_active = True
#while game_active == True:
#	print(f"User has {sum(user_list)} {user_list}")
#	print(f"Computer has {computer_list[0]}")
#	current_winner()
#	#user_turn
#	cont = input("Do you want another card? Enter Y or N:\n")
#	if cont == "Y":
#		choice = random.choice(cards)
#		user_list.append(choice)
#	else:
#		game_active = False
	
#dealer_turn
#if current_winner == "user":
#	game_active = True
#	while sum(computer_list) < 17:
#		choice = random.choice(cards)
#		computer_list.append(choice)
#		current_winner()
#else:
#	exit()

#current_winner()
#
#results()