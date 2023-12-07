def findWins(time, distance):
	t = 1
	wins = [0,0]
	while t * (time - t) < distance:
		t += 1
	wins[0] = t
	
	t = time
	while t * (time - t) < distance:
		t -= 1
	wins[1] = t

	return wins

with open('input6.txt', 'r') as inp:
	times = inp.readline().split()
	times.remove(times[0])
	time = ""
	for t in times:
		time += t
	time = int(time)
	
	distances = inp.readline().split()
	distances.remove(distances[0])
	distance = ""
	for d in distances:
		distance += d
	distance = int(distance)
	
	wins = findWins(time, distance)
	
	print(wins[1] - wins[0] + 2)
