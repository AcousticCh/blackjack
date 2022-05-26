#!usr/bin/env python
from random import choice
from subprocess import call
card_deck = {
	"1s": 1,
	"2s": 2,
	"3s": 3,
	"4s": 5,
	"6s": 6,
	"7s": 7,
	"8s": 8,
	"9s": 9,
	"10s": 10,
	"js": 10,
	"qs": 10,
	"ks": 10,
	"1d": 1,
	"2d": 2,
	"3d": 3,
	"4d": 5,
	"6d": 6,
	"7d": 7,
	"8d": 8,
	"9d": 9,
	"10d": 10,
	"jd": 10,
	"qd": 10,
	"kd": 10,
	"1h": 1,
	"2h": 2,
	"3h": 3,
	"4h": 5,
	"6h": 6,
	"7h": 7,
	"8h": 8,
	"9h": 9,
	"10h": 10,
	"jh": 10,
	"qh": 10,
	"kh": 10,
	"1c": 1,
	"2c": 2,
	"3c": 3,
	"4c": 5,
	"6c": 6,
	"7c": 7,
	"8c": 8,
	"9c": 9,
	"10c": 10,
	"jc": 10,
	"qc": 10,
	"kc": 10,
	}
cards = [
	"1s",
	"2s",
	"3s",
	"4s",
	"6s",
	"7s",
	"8s",
	"9s",
	"10s",
	"js",
	"qs",
	"ks",
	"1d",
	"2d",
	"3d",
	"4d",
	"6d",
	"7d",
	"8d",
	"9d",
	"10d",
	"jd",
	"qd",
	"kd",
	"1h",
	"2h",
	"3h",
	"4h",
	"6h",
	"7h",
	"8h",
	"9h",
	"10h",
	"jh",
	"qh",
	"kh",
	"1c",
	"2c",
	"3c",
	"4c",
	"6c",
	"7c",
	"8c",
	"9c",
	"10c",
	"jc",
	"qc",
	"kc",
	]
play_again = "y"
while play_again == "y":
	call("clear")
	player_hand = []
	dealer_hand = []
	while len(player_hand) < 2 and len(dealer_hand) < 2:
		player_card = choice(cards)
		dealer_card = choice(cards)
		player_hand.append(card_deck[player_card])
		dealer_hand.append(card_deck[dealer_card])
	
	another_card = "y"
	while another_card == "y":
		print(f"Your hand is {player_hand}")
		another_card = input("Would you like another card[y/n]: ").lower()
		if another_card == "y":
			player_card = choice(cards)
			player_hand.append(card_deck[player_card])
	
	while sum(dealer_hand) <= 13:
		dealer_card = choice(cards)
		dealer_hand.append(card_deck[dealer_card])
		
	if sum(player_hand) <= 21:
		if sum(player_hand) > sum(dealer_hand):
			print(f"Dealer hand equals {sum(dealer_hand)}")
			print(f"your hand equals {sum(player_hand)}")
			print("You Win!")
		elif sum(player_hand) < sum(dealer_hand):
			print(f"Dealer hand equals {sum(dealer_hand)}")
			print(f"your hand equals {sum(player_hand)}")
			print("You Lose")
	if sum(player_hand) > 21:
		print(f"Dealer hand equals {sum(dealer_hand)}")
		print(f"your hand equals {sum(player_hand)}")
		print("bust")
		
	if sum(dealer_hand) > 21:
		print(f"Dealer hand equals {sum(dealer_hand)}")
		print(f"your hand equals {sum(player_hand)}")
		print("dealer_bust you win")
		
	play_again = input("Would you like to play again? [y/n]: ")