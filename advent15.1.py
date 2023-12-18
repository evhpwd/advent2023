
with open('input15.txt', 'r') as inp:
	steps = inp.read().strip('\n').split(',')
	total = 0
	for step in steps:
		currentValue = 0
		for char in step:
			currentValue += ord(char)
			currentValue *= 17
			currentValue %= 256
		total += currentValue
	print(total)
