
with open('input8.txt', 'r') as inp:
	instructions = inp.readline().strip()
	inp.readline()
	lines = inp.read().split('\n')
	
	nodes = []
	order = []
	
	for l in range(len(lines)):
		order.append(lines[l].split(" = ")[0])
		nodes.append(lines[l].split(" = ")[1].strip("()").split(", "))
	
	going = True
	current = order.index("AAA")
	steps = 0
	
	while going:
		for i in instructions:
			steps += 1
			if i == 'R':
				current = order.index(nodes[current][1])
			else:
				current = order.index(nodes[current][0])
			if order[current] == "ZZZ":
				going = False
				break
	
	print(steps)
