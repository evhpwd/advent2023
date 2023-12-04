def getSurroundings(coords, length):
	surroundingCoords = []
	x, y = coords
	for i in range(-1,length+1):
		surroundingCoords.extend([(x-1,y+1), (x-1,y), (x-1,y-1)])
		x += 1
	return surroundingCoords
			

with open('input3.txt', 'r') as inp:
	line = inp.readline()
	numbers = []
	gears = []
	total = 0
	y = 0
	while line != "":
		curNum = ""
		x = 0
		for i in line:
			if i.isnumeric():
				curNum += i
			else:
				if curNum != "":
					numbers.append((curNum, (x-len(curNum),y)))
				if i == '*':
					gears.append((x ,y))
				curNum = ""
			x += 1
		line = inp.readline()
		y += 1
		
	adjacentGears = []

	for n in numbers:
		surroundingCoords = getSurroundings(n[1], len(n[0]))
		for g in gears:
			if g in surroundingCoords:
				for a in adjacentGears:
					if g in a:
						adjacentGears[adjacentGears.index(a)][2] += 1
						adjacentGears[adjacentGears.index(a)][0] *= int(n[0])
						break
				else:
					adjacentGears.append([int(n[0]), g, 1])

	for i in adjacentGears:
		if i[2] == 2:
			total += i[0]
	
	print(total)
