
def getHash(label):
	currentValue = 0
	for char in label:
		currentValue += ord(char)
		currentValue *= 17
		currentValue %= 256
	return currentValue

with open('input15.txt', 'r') as inp:
	
	lenses = inp.read().strip('\n').split(',')
	lensBoxes = {i:[] for i in range(256)}

	for lens in lenses:
		lens = lens.split('=')
		
		if len(lens) > 1:
			label, focalLength = lens
			box = getHash(label)
			
			for boxLens in lensBoxes[box]:
				index = lensBoxes[box].index(boxLens)
				
				if label == boxLens[0]:
					lensBoxes[box][index] = (label, focalLength)
					break
		
			else:
				lensBoxes[box].append((lens[0], lens[1]))
				
		else:
			label = lens[0].strip('-')
			box = getHash(label)
			for boxLens in lensBoxes[box]:
				if label == boxLens[0]:
					lensBoxes[box].remove(boxLens)
					break
	
	total = 0
	for box in lensBoxes:
		for lens in lensBoxes[box]:
			total += (box + 1) * (lensBoxes[box].index(lens) + 1) * int(lens[1])

	print(total)
