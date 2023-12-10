
from collections import Counter

def findNextStep(history):
	sequences = [[0]]
	sequences[0] += history
	for h in range(1, len(sequences[0])):
		s = 0
		while s < len(sequences):
			curSeq = sequences[s]
			if Counter(curSeq)[0] != len(curSeq):
				sequences.append([0])
				nextSeq = sequences[s+1]
				for n in range(2, len(curSeq)):
					sequences[s+1].append(curSeq[n]-curSeq[n-1])
			else:
				for h in range(len(sequences)-1,0,-1):
					curSeq = sequences[h-1]
					prevSeq = sequences[h]
					curSeq[0] += curSeq[1] - prevSeq[0]
				return sequences[0][0]
			s += 1

with open('input9.txt', 'r') as inp:
	histories = inp.read().split('\n')
	for h in range(len(histories)):
		histories[h] = histories[h].split()
		histories[h] = list(map(int, histories[h]))
	
	total = 0
	for history in histories:
		total += findNextStep(history)
	
	print(total)
