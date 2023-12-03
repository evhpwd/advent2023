with open('input1.txt', 'r') as inp:
	line = inp.readline()
	firstNum = 0
	lastNum = 0
	total = 0
	while line != "":
		for i in range(0, len(line)):
			if line[i].isnumeric():
				firstNum = int(line[i]) * 10
				break
		for i in range(len(line)-1, -1, -1):
			if line[i].isnumeric():
				lastNum = int(line[i])
				break
		total += firstNum + lastNum
		line = inp.readline()
	print(total)
