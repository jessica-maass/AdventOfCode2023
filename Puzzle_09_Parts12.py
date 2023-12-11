import sys
import clr
clr.AddReference('ProtoGeometry')

def GetDeltas (sequence, n=0, dir="forward"):
	# for the list of nums, return the deltas between them
	zeroes = 0		# int to see if deltas all zero or not
	deltas = []		# list to store deltas between nums in sequence

	# get the delta between each num and the next num
	for i in range(0, len(sequence)-1):
		n1 = sequence[i]
		n2 = sequence[i+1]
		delta = n2 - n1
		deltas.append(delta)
		
		if delta == 0:
			zeroes += 1
	
	# PART 1 | look for next num in sequence
	if dir == "forward":
		# if found the final deltas, insert 0 at end and begin moving back
		if zeroes == len(deltas):
			deltas.append(0)
			return deltas
		# otherwise get the deltas of the deltas
		else:
			nextDeltas = GetDeltas(deltas, n+1)
			next = nextDeltas[-1] + deltas[-1]
			deltas.append(next)
			
			# if not at outermost level, return revised delta list
			if n != 0:
				return deltas
			# otherwise calculate the next num in sequence
			else:
				final = deltas[-1] + sequence[-1]
				return final
	
	# PART 2 | look for prev num in sequence
	elif dir == "backward":
		# if found the final deltas, insert 0 at start and begin moving back
		if zeroes == len(deltas):
			deltas.insert(0,0)
			return deltas
		
		# otherwise get the deltas of the deltas
		else:
			prevDeltas = GetDeltas(deltas, n+1, dir)
			prev = deltas[0] - prevDeltas[0]
			deltas.insert(0, prev)
			
			# if not at outermost level, return revised delta list
			if n != 0:
				return deltas
			# else calculate the previous num in sequence
			else:
				first = sequence[0] - deltas[0]
				return first

#################################
input = IN[0]

histories = []		# list of starting histories
finalSum = 0		# PART 1 | sum of next nums in histories
firstSum = 0		# PART 2 | sum of prev nums in histories
#################################

# split up input into histories
for line in input:
	history = []
	for num in line.split():
		history.append(int(num.strip()))
	histories.append(history)

# for each history, get the next and prev numbers
for history in histories:	
	# PART 1 | find the next expected value and sum them
	sum = GetDeltas(history)
	finalSum += sum
	
	# PART 2 | find the first expected value and sum them
	sum = GetDeltas(history, 0, "backward")
	firstSum += sum

OUT = "FINALSUM: %s" %finalSum, "FIRSTSUM: %s" %firstSum
