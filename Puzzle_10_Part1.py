import sys
import clr
clr.AddReference('ProtoGeometry')

def GetNeighbors (curr):
	# given the path, determine the next viable path(s)
	currPos = curr.split(",")[-1]				# current position = last pipe in path
	row = int(currPos.split(":")[0])		# row of current pipe in map
	col = int(currPos.split(":")[1])		# column of current pipe in map
	currPipe = map[row][col]		# string symbol of current pipe
	visited = set()			# set to store pipes already visited so far
	nextPaths = []			# list of next valid paths vound

	# is this the strating pipe
	isStart = False
	if currPipe == "S":
		isStart = True

	# add all previous pipe segments to visited set for the current pipe
	if "," in curr:
		for prev in curr.split(","):
			visited.add(prev)

	# create vectors for row, col, and direction
	rowVect = [-1, 1, 0, 0]
	colVect = [0, 0, -1, 1]
	dirVect = ["U", "D", "L", "R"]	# location of the next neighbor

	# get neighbors and see if valid
	for i in range(0, 4):
		row1 = row + rowVect[i]
		col1 = col + colVect[i]
		dir = dirVect[i]
		next = "%s:%s" %(row1, col1)

		# check validity of the neighbor
		search = True
		if row1 < 0 or col1 < 0:
			search = False
		elif row1 >= rowMax or col1 >= colMax:
			search = False
		elif next in visited:
			search = False
		elif next in checked:
			search = False
		else:
			nextPipe = map[row1][col1]
			if nextPipe == ".":
				search = False
		
		# if location is valid, see if pipe is connecting
		if search == True:
			isNeighbor = False
			valid = []
			# get current pipe if it's the starting pipe
			if isStart == True:
				if dir == "U" or dir == "D":
					currPipe = "|"
				elif dir == "L" or dir == "R":
					currPipe = "-"
				
			# see if neighbor pipe is valid connector based on connecting direction
			if dir == "U":
				valid = up[currPipe]
			elif dir == "D":
				valid = down[currPipe]
			elif dir == "L":
				valid = left[currPipe]
			elif dir == "R":
				valid = right[currPipe]
		
			# if next pipe in valid list of connectors, it's a neighbor
			if nextPipe in valid:
				isNeighbor = True
			
			# if next pipe is valid for curr pipe, add to the path
			if isNeighbor == True:
				nextPath = curr + "," + next
				nextPaths.append(nextPath)
				pipesNext[0] += 1
				checked.add(next)
	
	return nextPaths

#################################
input = IN[0]

map = []			# list of map rows
rowMax = len(input)		# max row of map
colMax = len(input[0])	# map col of map
start = ""		# starting pipe position
paths = []		# list of paths to iterate through
step = 1			# step for iterating
steps = 50000		# last step for iterating

pipesLeft = 0		# int to track how many pipes left in curr step
pipesNext = [0]		# int to track how many pipes in the next step
stepCount = 1		# SOLUTION | how far from start is the furthest pipe
checked = set()		# set to store pipes already checked

# visualize the map of pipes
ends = set()
visual = []	
pipes = {"F":"╔", "L":"╚", "7":"╗", "J":"╝", "|":"║", "-":"═", ".":" ", "S":"S"}

# dictionaries of pipes and valid connectors from right, left, up, and down sides
right = {"F":["7","J","-"], "L":["J","7","-"], "7":[],            "J":[],            "|":[],        "-":["7","J","-"]}
left  = {"F":[],            "L":[],            "7":["F","L","-"], "J":["L","F","-"], "|":[],        "-":["F","L","-"]}
up    = {"F":[],            "L":["F","7","|"], "7":[],            "J":["F","7","|"], "|":["7","F","|"], "-":[]}
down  = {"F":["L","J","|"], "L":[],            "7":["L","J","|"], "J":[],            "|":["L","J","|"], "-":[]}
#################################

# set up the map and collect the starting pipe
for r in range(0, len(input)):
	map.append(input[r])
	for c in range(0, len(input[r])):
		if input[r][c] == "S":
			debug.append("[[0]] --> Start: (%s, %s)" %(r, c))
			start = "%s:%s" %(r,c)
			
# get starting paths
paths = GetNeighbors(start)
pipesLeft = len(paths)
pipesNext = [0]
checked.add(start)
for path in paths:
	ends.add(path.split(",")[-1])

# run through until checked each path
while len(paths) > 0 and step <= steps:
	path = paths.pop(0)
	last = path.split(",")[-1]

	# decrease counter and check for neighbors
	pipesLeft -= 1
	if path not in checked:
		neighbors = GetNeighbors(path)

		# if found neighbors, add to list
		if len(neighbors) > 0:
			for neighbor in neighbors:
				paths.append(neighbor)

	# if no more paths, found the end
	if len(paths) == 0:
		break

	# if end of current counter, reset with next pipes
	if pipesLeft == 0:
		pipesLeft = pipesNext[0]
		pipesNext = [0]

		# visualize the current ends of pipe paths
		ends.clear()
		for path in paths:
			ends.add(lastPipe)

		# increase overall step count 
		stepCount += 1
	
	step += 1

# VISUALIZE THE MAP AND CURRENT POSITION
for r in range(0, len(input)):
	line = input[r]
	map.append(line)
	row = ""
	for c in range(0, len(line)):
		char = line[c]
		if "%s:%s" %(r,c) not in ends:
			row += pipes[char]
		else:
			row += "X"
	visual.append(row)

OUT = stepCount, visual
