with open('input1.txt', 'r') as inp:
	line = inp.readline()
	firstNum = 0
	lastNum = 0
	total = 0
	digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	while line != "":
		firstNum = 0
		lastNum = 0
		for i in range(0, len(line)):
			if line[i].isnumeric():
				firstNum = line[i]
			else:
				for d in digits:
					if d in line[i:i+len(d)]:
						firstNum = digits.index(d)+1
						break
			if firstNum != 0:
				break
		for i in range(len(line)-1, -1, -1):
			if line[i].isnumeric():
				lastNum = line[i]
			else:
				for d in digits:
					if d in line[i-len(d):i]:
						lastNum = digits.index(d)+1
						break
			if lastNum != 0:
				break
		total += int(firstNum)*10 + int(lastNum)
		line = inp.readline()
	print(total)
