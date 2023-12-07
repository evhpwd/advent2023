def findWins(time, distance):
	t = 1
	wins = 0
	while t < time:
		if t * (time - t) > distance:
			wins += 1
		t += 1
	return wins

with open('input6.txt', 'r') as inp:
	times = inp.readline().split()
	times.remove(times[0])
	times = list(map(int, times))
	
	distances = inp.readline().split()
	distances.remove(distances[0])
	distances = list(map(int, distances))
	
	total = 1
	
	for time in times:
		total *= findWins(time, distances[times.index(time)])
	
	print(total)
