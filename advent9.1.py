
from collections import Counter

def findNextStep(history):
	sequences = [history.copy()]
	for h in range(len(sequences[0])):
		s = 0
		while s < len(sequences):
			curSeq = sequences[s]
			if Counter(curSeq)[0] != len(curSeq):
				sequences.append([])
				nextSeq = sequences[s+1]
				for n in range(1, len(curSeq)):
					sequences[s+1].append(curSeq[n]-curSeq[n-1])
			else:
				for h in range(len(sequences)-1,0,-1):
					curSeq = sequences[h-1]
					prevSeq = sequences[h]
					curSeq.append(curSeq[len(curSeq)-1] + prevSeq[len(prevSeq)-1])
				return sequences[0][len(sequences[0])-1]
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
