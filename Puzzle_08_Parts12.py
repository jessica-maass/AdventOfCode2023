import sys
import clr
clr.AddReference('ProtoGeometry')

def Navigate1 (start):
	# PART 1 | run through the nodes until reach "ZZZ"
	curr = start		# current node we're in, begin at "AAA"
	result = False		# bool to determine if found exit
	moves = []			# list of movements to make
	step = 1			# current step
	steps = 20000		# max step
	
	# set up initial movement instructions
	for char in instructions:
		moves.append(char)
	
	# run through X steps until reach the end "ZZZ"
	while curr != "ZZZ" and step < steps:
		# based on the movement instruction, get whether L or R movement
		i = 0
		move = moves.pop(0)
		if move == "R":
			i = 1
		
		# move L or R and get next node
		next = nodes[curr][i]
		curr = next
		
		# if found the end, exit and return step
		if curr == "ZZZ":
			result = True
			break
		
		# if out of movement, reset the list
		if len(moves) == 0:
			for char in instructions:
				moves.append(char)
		
		step += 1
	
	return result, step

def Navigate2 (starting):
	# PART 2 | start at all nodes ending in A; go until reach all nodes ending in Z
	currs = ""			# current nodes we're in
	result = False		# bool to determine if end found
	moves = []			# list of movements to make
	step = 1			# current step
	steps = 250000		# max step
	finalStep = 1		# SOLUTION | final step based on LCM
	
	# set up initial movement instructions
	for char in instructions:
		moves.append(char)
	
	# set up initial current nodes
	for start in starting:
		currs += "%s," %start
	currs = currs[:-1]
	
	# run through X steps until found first step for each ending node
	while result == False and step <= steps:
		# based on movement instruction, get R or L direction
		i = 0
		move = moves.pop(0)
		if move == "R":
			i = 1
		
		# move the current nodes to their next nodes based on movement
		nexts = ""
		for curr in currs.split(","):
			next = nodes[curr][i]
			nexts += "%s," %next
		currs = nexts[:-1]
		
		# determine if any new positions are the exits (end with "Z")
		ends = 0
		exits = ""
		for curr in currs.split(","):
			if curr[-1] == "Z":
				ends += 1
				exits += curr
				
				# if current is an exit node, collect the step count
				if curr not in timeToExit.keys():
					timeToExit[curr] = step
		
		# if found all the step counts for the exits, break out
		if len(timeToExit) == len(starting):
			result = True
			break	
		
		# reset movement instructions if ran out
		if len(moves) == 0:
			for char in instructions:
				moves.append(char)
		
		step += 1	
	
	# if found all exit steps, calculate the LCM for the final result
	if result == True:
		finalStep = ReduceTime(timeToExit.values())
	
	return result, finalStep

def ReduceTime (times):
	# LCM: get all primes for each exit time, and multiple to get final answer
	finalTime = 1		# SOLUTION | final time
	primes = []			# list of primes
	factors = set()		# set of prime factors for the times
	
	# get list of primes:
	primes = GetPrimes (300)
	
	# run through each exit time and find unique prime factors
	for time in times:
		for prime in primes:
			if time % prime == 0:
				debug.append("%s / %s" %(time, prime))
				factors.add(prime)
	
	# multiply all prime factors together to get solution
	for factor in factors:
		finalTime *= factor
	return finalTime
	
def GetPrimes (max):
	# get all primes from 1 to max
	primes = []
	for num in range(2, max):
		isPrime = True
		for div in range(2,num):
			if num % div == 0:
				isPrime = False
		if isPrime == True:
			primes.append(num)
	return primes

#################################
input = IN[0]

instructions = ""	# list of R L instructions
nodes = {}			# dict of nodes and its connectors
results1 = []		# PART 1 | how many steps to reach ZZZ

starts = []			# list of starting nodes (ends with "A")
timeToExit = {}		# dict to store how long to each exit
results2 = []		# PART 2 | how many steps to reach all ##Z
#################################

# split up input into instructions and node->connections
for line in input:
	if "=" not in line:
		instructions = line.strip()
	else:
		name = line.split(" = ")[0]
		connects = line.split("(")[1][:-1].split(", ")
		nodes[name] = connects
		
		# collect starting nodes (nodes ending with "A")
		if name[-1] == "A":
			starts.append(name)

# PART 1 | go from node "AAA" to node "ZZZ"
results1 = Navigate1("AAA")

# PART 2 | go from all nodes ending "A" to all nodes ending "Z"
results2 = Navigate2(starts)

OUT = results1, results2
