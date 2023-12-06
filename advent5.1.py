import math

def findDest(smap, src):
	for line in smap:
		if src >= line[1] and src <= line[1]+line[2]:
			src += line[0]-line[1]
			return src
	return src


with open('input5.txt', 'r') as inp:
	seeds = inp.readline()[7:].split()

	inp.readline()
	maps = inp.read().split("\n\n")
	i = 0
	while i < len(maps):
		maps[i] = maps[i].split('\n')
		maps[i].remove(maps[i][0])
		n = 0
		while n < len(maps[i]):
			maps[i][n] = maps[i][n].split()
			maps[i][n] = list(map(int, maps[i][n]))
			n += 1
		i += 1

	lowestLoc = math.inf

	for s in seeds:
		src = int(s)
		for smap in maps:
			src = findDest(smap, src)
		if lowestLoc > src:
			lowestLoc = src
	
	print(lowestLoc)
