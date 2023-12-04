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
	symbols = []
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
				if i != '.' and i != '\n':
					symbols.append((i,(x,y)))
				curNum = ""
			x += 1
		line = inp.readline()
		y += 1

	for n in numbers:
		surroundingCoords = getSurroundings(n[1], len(n[0]))
		for s in symbols:
			if s[1] in surroundingCoords:
				total += int(n[0])
				break
			
	print(total)
				
