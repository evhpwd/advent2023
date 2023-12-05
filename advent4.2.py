def calcWins(card):
	winningNums = card[0].split()
	scratchNums = card[1].split()
	count = 0
	for s in scratchNums:
		if s in winningNums:
			count += 1
	return count


with open('input4.txt', 'r') as inp:
	cards = inp.read().split('\n')
	wins = []		#
	total = 0
	
	for i in cards:
		i = i[7:]
		card = i.split('|')
		if card != ['']:
			wins.append(calcWins(card))
	
	cardFreqs = [1]*len(wins)
	i = 0
	while i < len(cardFreqs):
		for n in range(1, wins[i]+1):
			if i+n < len(cardFreqs):
				cardFreqs[i+n] += cardFreqs[i]
		i += 1
	
	for i in cardFreqs:
		total += i
	print(total)
