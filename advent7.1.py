
from collections import Counter

def checkHand(hand):
	cardFreqs = Counter(hand).values()
	
	if 5 in cardFreqs:
		return 6
	elif 4 in cardFreqs:
		return 5
	elif 3 in cardFreqs:
		if 2 in cardFreqs:
			return 4
		else:
			return 3
	elif 2 in cardFreqs:
		if len(cardFreqs) == 3:
			return 2
		else:
			return 1
	else:
		return 0


with open('input7.txt', 'r') as inp:
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	hands = inp.read().split('\n')
	
	for x in range(len(hands)):
		hands[x] = hands[x].split()
		newHand = []
		for c in range(len(hands[x][0])):
			newHand.append(cards.index(hands[x][0][c]))
		hands[x][0] = newHand
		hands[x][1] = int(hands[x][1])
		hands[x].append(0)
		
	for hand in hands:
		hands[hands.index(hand)][2] = checkHand(hand[0])
	
	hands.sort(key=lambda x: (x[2], x[0]))
	
	total = 0
	for hand in hands:
		total += hand[1] * (hands.index(hand) + 1)

	print(total)
	
	
