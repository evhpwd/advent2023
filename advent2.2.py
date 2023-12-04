def findMins(turns):
	redNum = 0
	greenNum = 0
	blueNum = 0
	for i in turns:
		turn = i.split(',')
		for n in turn:
			num, colour = n.split()
			num = int(num)
			if colour == "red" and num > redNum:
				redNum = num
			elif colour == "green" and num > greenNum:
				greenNum = num
			elif colour == "blue" and num > blueNum:
				blueNum = num
	return redNum, greenNum, blueNum

with open('input2.txt', 'r') as inp:
	game = inp.readline().split(':')
	total = 0
	while game != ['']:
		turns = game[1].split(';')
		redNum, greenNum, blueNum = findMins(turns)
		total += redNum * greenNum * blueNum
			
		game = inp.readline().split(':')
	print(total)
