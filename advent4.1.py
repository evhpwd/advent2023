with open('input4.txt', 'r') as inp:
	nums = inp.readline()[7:].split('|')
	total = 0
	while nums != ['']:
		winningNums = nums[0].split()
		scratchNums = nums[1].split()
		count = 0
		for s in scratchNums:
			if s in winningNums:
				count += 1
		if count != 0:
			total += 2 ** (count-1)
		nums = inp.readline()[7:].split('|')
	print(total)
