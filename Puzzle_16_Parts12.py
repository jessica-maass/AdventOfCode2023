def Beam (beam):
	# for the given beam, see where the beam will go to next
	row = beam[0]			# the curr beam's row in map
	col = beam[1]			# the curr beam's col in map
	dir = beam[2]			# the curr beam's moving direction
	tile = map[row][col]	# the curr beam's tile on map
	
	# based on tile, see where the beam will travel next
	for nextDir in move[dir][tile]:
		vect = dirs[nextDir]	# next beam's moving direction
		row1 = row + vect[0]	# next beam's row in map
		col1 = col + vect[1]	# next beam's col in map
		
		# see if next tile is in the map
		if row1 >= 0 and col1 >= 0 and row1 < rowMax and col1 < colMax:
			
			# see if the next tile path is new or has been traveled already
			path = "%s,%s,%s|%s,%s,%s" %(row,col,dir, row1,col1,nextDir)
			if path not in prevPaths:
				queue.append([row1, col1, nextDir])
				energized.add("%s,%s" %(row1, col1))
				prevPaths.add(path)

#################################
input = IN[0]

map = []		# list of input to run through
rowMax = len(input)
colMax = len(input[0])

start1 = [0,0,"R"]	# PART 1 | starting position of beam
starting = []		# PART 2 | starting tiles (all edges)
queue = []			# queue of next beams to run through
prevPaths = set()	# set to store previous movements as (curr-next) to reduce queue

steps = 100000		# int of steps to run through

# dictionaries to store moving directions
dirs = {"R":[0,1], "L":[0,-1], "D":[1,0], "U":[-1,0]}
moveR = {".": "R", "/": "U", "\\": "D", "|": "UD", "-": "R"}
moveL = {".": "L", "/": "D", "\\": "U", "|": "UD", "-": "L"}
moveU = {".": "U", "/": "R", "\\": "L", "|": "U", "-": "LR"}
moveD = {".": "D", "/": "L", "\\": "R", "|": "D", "-": "LR"}
move = {"R": moveR, "L": moveL, "U": moveU, "D": moveD}

energized = set()	# set to store unique tiles landed on
part1Energized = 0	# PART 1 SOL | unique tiles found from start1 beam
maxEnergized = 0	# PART 2 SOL | unique tiles found from any edge start beam
#################################

# set up the map from the input
for line in input:
	map.append(line)

# PART 1 | assign start to queue and solution
queue.append(start1)
energized.add("%s,%s" %(start1[0],start1[1]))

# PART 2 | assign starting queue 
c = range(0, colMax)
for c in range(0, colMax):
	starting.append([0, c, "D"])
	starting.append([(rowMax-1), c, "U"])
for r in range(0, rowMax):
	starting.append([r, 0, "R"])
	starting.append([r, (colMax-1), "L"])

# run through X steps
count = 0
for start in starting:		# PART 2 | run through all possible start positions
	# for each starting position, reset the various variables
	queue.Clear()
	prevPaths.clear()
	energized.clear()
	count += 1
	
	# initialize with current starting position
	queue.append(start)
	energized.add("%s,%s" %(start[0], start[1]))
	
	# run through beam to get count of tiles passed
	step = 0
	while step < steps and len(queue) > 0:
		Beam( queue.pop(0) )
		step += 1
	
	# if new max found, save it
	if len(energized) > maxEnergized:
		maxEnergized = len(energized)
	
	# save the solution for PART 1
	if start == start1:
		part1Energized = len(energized)

OUT = part1Energized, maxEnergized
