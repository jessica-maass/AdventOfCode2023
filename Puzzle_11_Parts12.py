import sys
import clr
clr.AddReference('ProtoGeometry')

def Expand (map, empties):
	# expand the universe where a row or col has no galaxies
	emptyRows = []		# list of empty row indexes
	emptyCols = []		# list of empty column indeces
	galaxies = {}		# dictionary of galaxies by name|position
	galaxyCount = 1		# count of galaxies, used as galaxy name
	
	# run through the map and count galaxies in each row and column
	cCount = {}		# count galaxies in columns
	for r in range(0, len(map)):
		line = map[r]
		rCount = 0		# count galaxies in rows
		for c in range(0, len(line)):
			if c not in cCount.keys():
				cCount[c] = 0
			
			# if galaxy, add to the row/col counts
			if line[c] == "#":
				rCount += 1
				cCount[c] += 1
				
				# save galaxy position in dict
				pos = "%s,%s" %(r,c)
				galaxies[galaxyCount] = pos
				galaxyCount += 1
		
		# if no galaxies in the row, collect empty index
		if rCount == 0:
			emptyRows.append(r)
	
	# if not galaxies in each column, collect empty index
	for r in cCount.keys():
		if cCount[r] == 0:
			emptyCols.append(r)
	
	# reverse empty row/col lists for adding in new blanks
	emptyRows.reverse()
	emptyCols.reverse()
	
	# insert empty rows 
	for row in emptyRows:
		for galaxy in galaxies.keys():
			oldPos = galaxies[galaxy]
			r = int(oldPos.split(",")[0])
			c = int(oldPos.split(",")[1])
			
			# expand galaxy if in the r-coordinate
			if r >= row:
				newRow = r + empties
				newPos = "%s,%s" %(newRow, c)
				galaxies[galaxy] = newPos
	
	# insert empty cols
	for col in emptyCols:
		for galaxy in galaxies.keys():
			oldPos = galaxies[galaxy]
			r = int(oldPos.split(",")[0])
			c = int(oldPos.split(",")[1])
			
			# expand the galaxy if in the c-coordinate
			if c >= col:
				newCol = c + empties
				newPos = "%s,%s" %(r, newCol)
				galaxies[galaxy] = newPos

	return galaxies

def DistanceTo (part, name1, name2):
	# calculate the distance between two galaxies
	pos1 = ""		# coords of galaxy 1
	pos2 = ""		# coords of galaxy 2
	if part == 1:
		pos1 = galaxies1[name1]
		pos2 = galaxies1[name2]
	elif part == 2:
		pos1 = galaxies2[name1]
		pos2 = galaxies2[name2]
	
	# get x and y coords of galaxy
	x1 = int(pos1.split(",")[0])
	y1 = int(pos1.split(",")[1])
	x2 = int(pos2.split(",")[0])
	y2 = int(pos2.split(",")[1])
	
	# calculate the x and y deltas, then sum up the total distance
	deltaX = abs(x1 - x2)
	deltaY = abs(y1 - y2)
	delta = deltaX + deltaY
	
	return delta

#################################
input = IN[0]

emptyInsert1 = 1		# int of empty rows/cols to add
galaxies1 = {}	# PART 1 | dict of galaxies by their position
sumDist1 = 0	# PART 1 | sum of distances with 2x expansion

emptyInsert2 = 1000000-1	# int of empty rows/cols to add
galaxies2 = {}	# PART 2 | dist of galaxies by their position
sumDist2 = 0	# PART 2 | sum of distances with 1,000,000 expansion
#################################

# get dict of galaxies
galaxies1 = Expand(input, emptyInsert1)
galaxies2 = Expand(input, emptyInsert2)

# get all distances between galaxy A and galaxy B for all galaxies
a = 1
while a < len(galaxies1.values())+1:
	b = a + 1
	while b < len(galaxies1.values())+1:
		dist1 = DistanceTo(1, a, b)
		sumDist1 += dist1
		
		dist2 = DistanceTo(2, a, b)
		sumDist2 += dist2
		
		b += 1
	a += 1

OUT = sumDist1, sumDist2
