def Roll(row):
	# roll rocks northwards
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
				

def PrintMap ():
	# print currnt map of rocks
	map = []
	for r in range(0, len(input)):
		row = ""
		for c in range(0, len(input[0])):
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

cubes = {}		# dict to track cube rocks per column
rounds = {}		# dict to track round rocks per column
totalLoad = 0	# SOLUTION | total load on to row
#################################

# initalize cubes and rounds rocks dictionaries
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
for row in range(1, len(input)):
	Roll(row)

# get sum of load on topmost beam
for row in range(0, len(input)):
	if row in rounds.keys():
		load = len(rounds[row]) *(len(input) - row)
		totalLoad += load

OUT = totalLoad, mapStart, PrintMap()
