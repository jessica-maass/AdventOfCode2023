def Roll (row):
	# roll all rocks in the map up as far as possible
	moved = []		# list to store which rocks in this row move
	
	# check each rock in this row, if there are any
	if row in rounds.keys():
		roundRocks = rounds[row]
		
		# for each rock, see how far it can roll up
		for col in roundRocks:
			maxHeightCube = row
			maxHeightRound = row
			obstruct = False
			
			# collect objects above the rock
			colAbove = []
			while len(colAbove) < row:
				above = "."
				# check for other round rocks
				row1 = len(colAbove)
				if row1 in rounds.keys():
					if col in rounds[row1]:
							above = "O"
			
				# check for cubes above
				if col in cubes.keys():
					if row1 in cubes[col]:
						above = "#"
				
				# collect objects above current rock
				colAbove.append(above)
			
			# determine how far this rock can roll
			newRow = row
			while len(colAbove) > 0 and newRow > 0:
				above = colAbove.pop()
				if above == ".":
					newRow -= 1
				elif above == "O" or "#":
					break
			
			# move the rock to the new roll
			if newRow != row:
				moved.append([row, newRow, col])
	
		# move the rocks if any can
		if len(moved) > 0:
			for rock in moved:
				row = rock[0]
				newRow = rock[1]
				col = rock[2]
				
				# remove rocks from the current row
				currRow = rounds[row]
				currRow.remove(col)
				rounds[row] = currRow
				
				# add rocks to the new row
				if newRow not in rounds.keys():
					rounds[newRow] = []
				nextRow = rounds[newRow]
				nextRow.append(col)
				nextRow.sort()
				rounds[newRow] = nextRow

def Rotate (rotLength):
	# PART 2: rotate counterclockwise for each cycle (NWSE)
	# get the current map and rotate it clockwise	
	rows = mapSize[rotLength%2]
	cols = mapSize[rotLength%2]
	mapOrig = PrintMap(rows, cols)
	mapTrans = []
	for c in range(0, cols):
		newRow = []
		for r in range(0, rows):
			newRow.append(mapOrig[r][c])
		newRow.reverse()
		mapTrans.append(newRow)

	# with the new map, determine new positions of round rocks
	newRounds = {}
	for row in range(0, len(mapTrans)):
		newRounds[row] = []
		for col in range(0, len(mapTrans[0])):
			char = mapTrans[row][col]
			if char == "O":
				newRound = newRounds[row]
				newRound.append(col)
				newRounds[row] = newRound
	
	# with the new map, determine new positions of cube rocks
	newCubes = {}
	for col in range(0, len(mapTrans[0])):
		newCubes[col] = []
		for row in range(0, len(mapTrans)):
			char = mapTrans[row][col]
			if char == "#":
				newCube = newCubes[col]
				newCube.append(row)
				newCubes[col] = newCube
	
	return [newRounds, newCubes]

def PrintMap (rows = 0, cols = 0):
	# print currnt map of rocks
	if rows == 0:
		rows = lenR
	if cols == 0:
		cols = lenC
	map = []
	for r in range(0, rows):
		row = ""
		for c in range(0, cols):
			char = "."
			if c in cubes.keys():
				if r in cubes[c]:
					char = "#"
			if r in rounds.keys():
				if c in rounds[r]:
					char = "O"
			row += char
		map.append(row)
	
	return map

#################################
input = IN[0]

lenR = len(input)
lenC = len(input[0])
mapSize = [lenR, lenC, lenR, lenC]

cubes = {}		# dict to track cube rocks per column
rounds = {}		# dict to track round rocks per column
totalLoad = 0	# SOLUTION | total load on to row

cycles = 1000000000		# PART 2: how many times to cycle rotations
pastCycle = [-1, -1]	# list of ints of first and last cycles in repetition
pastCycles = set()		# set to store previous cycles maps
pastCyclesNum = {}		# dict to store previous cycles number
pastCyclesMap = {}		# dict to store previous cycles maps
#################################

# set up initial round and cube rock dicionaries
for r in range(0, len(input)):
	line = input[r]
	for c in range(0, len(line)):
		char = line[c]
		
		if char == "#":
			if c not in cubes.keys():
				cubes[c] = []
			cubesC = cubes[c]
			cubesC.append(r)
			cubes[c] = cubesC
		
		if char == "O":
			if r not in rounds.keys():
				rounds[r] = []
			roundsC = rounds[r]
			roundsC.append(c)
			rounds[r] = roundsC

# run through each row and move the rocks up
mapStart = PrintMap()
repeat = False
cycle = 1
while cycle <= cycles and repeat == False:
	# for each cycle, rotate four times clockwise
	for rotate in range(0, 4):
		rotLen = mapSize[rotate]
		for row in range(1, rotLen):
			Roll (row)
		
		# rotate the board
		newDicts = Rotate(rotLen)
		rounds = newDicts[0]
		cubes = newDicts[1]
		
	# store current map
	currMap = ",".join(PrintMap())
	
	# check if current map has been seen already
	if currMap in pastCycles:
		repeat = True
	else:
		pastCycles.add(currMap)
		pastCyclesNum[currMap] = cycle
		pastCyclesMap[cycle] = currMap
	
	# if duplicate map found, record cycle nums and exit
	if repeat == True:
		match = pastCyclesNum[currMap]
		pastCycle = [match, cycle]
		break
	
	cycle += 1

# get sum of load on topmost beam
if pastCycle[0] != -1:
	first = pastCycle[0]			# first cycle in repetition
	last = pastCycle[1] - 1			# last cycle in repetition
	cycleLength = last - first + 1	# length of repetition
	
	# find corresponding cycle in repetition to the total cycles
	matchCycle = first + (cycles - first) % cycleLength
	map = pastCyclesMap[matchCycle].split(",")
	
	# calc total load on northmost beam
	for r in range(0, lenR):
		row = map[r]
		for char in row:
			if char == "O":
				totalLoad += (lenR - r)

OUT = totalLoad, mapStart, PrintMap()
