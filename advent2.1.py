def testPossible(turn):
	for n in turn:
		num, colour = n.split()
		num = int(num)
		if colour == "red" and num > 12:
			return False
		elif colour == "green" and num > 13:
			return False
		elif colour == "blue" and num > 14:
			return False
	return True

with open('input2.txt', 'r') as inp:
	game = inp.readline().split(':')
	total = 0
	while game != ['']:
		possible = True
		turns = game[1].split(';')
		for i in turns:
			turn = i.split(',')
			if not testPossible(turn):
				possible = False
				break
		if possible:
			total += int(game[0].split()[1])
		game = inp.readline().split(':')
	print(total)
