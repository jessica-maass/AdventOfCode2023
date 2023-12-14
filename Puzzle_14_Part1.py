import sys
import clr
clr.AddReference('ProtoGeometry')

def TiltNS (r, dir):
	# tilt all the rocks towards the north (up) or south (down)
	row = dish[r]		# curr row looking at
	roundRocks = []		# list of index of round rocks
	rolled = []			# list of index of rocks that rolled up/down
	
	# get index of all round rocks in curr row
	for o in range(0, len(row)):
		object = row[o]
		if object == "O":
			roundRocks.append(o)
	
	# see if each roundrock can move north
	while len(roundRocks) > 0:
		round = roundRocks.pop(0)
		newPos = r
		
		# roll rock north until hit cube rock or top row
		if dir == "north":
			above = r-1
			while above >= 0:
				objAbove = dish[above][round]
				
				# see if roll into static rock or into free space
				if objAbove == "#":
					break
				elif objAbove == ".":
					newPos = above
				above -= 1
		
		# roll rock south until hit cube or bott row
		elif dir == "south":
			below = r + 1
			while below < len(dish):
				objBelow = dish[below][round]
				
				if objBelow == "#":
					break
				elif objBelow == ".":
					newPos = below
				below += 1
		
		# if found a new position, add round rock to the new row
		if newPos != r:
			prevRow = dish.pop(newPos)
			newRowL = prevRow[0:round]
			newRowR = prevRow[round+1:]
			newRow = newRowL + "O" + newRowR
			dish.insert(newPos, newRow)
			rolled.append(round)
	
	# remove rolled rocks from current row
	if len(rolled) > 0:
		for rock in rolled:	
			currRowL = row[0:rock]
			currRowR = row[rock+1:]
			row = currRowL + "." + currRowR
		dish.pop(r)
		dish.insert(r, row)

def TiltWE (c, dir):
	# tilt all the rocks towards the west (left) or east (right)
	col = []			# curr column looking at
	roundRocks = []		# list of index of round rocks in curr col
	rolled = []			# list of indx of round rocks that roll right/left

	# get current column to look at
	for o in range(0, len(dish)):
		row = dish[o]
		col.append(row[c])
		if row[c] == "O":
			roundRocks.append(o)

	# for each round rock in col, see if can move left/right
	while len(roundRocks) > 0:
		round = roundRocks.pop(0)
		newPos = c

		# see if rock can move west/left
		if dir == "west":
			left = c - 1
			while left >= 0:
				objLeft = dish[round][left]
				if objLeft == "#":
					break
				elif objLeft == ".":
					newPos = left
				left -= 1

		# see if rock can move east/right
		elif dir == "east":
			right = c + 1
			while right < len(dish[0]):
				objRight = dish[round][right]
				if objRight == "#":
					break
				elif objRight == ".":
					newPos = right
				right += 1

		# if rock can move, move it to new position in dish
		if newPos != c:
			prevRow = dish.pop(round)
			newRowL = prevRow[0:newPos]
			newRowR = prevRow[newPos+1:]
			newRow = newRowL + "O" + newRowR
			dish.insert(round, newRow)		
			rolled.append(round)

	# for all rolled rocks, remove them from the col
	if len(rolled) > 0:
		for rock in rolled:	
			col[rock] = "."
		for i in range (0, len(dish)):
			row = dish[i]
			currRowL = row[0:c]
			currRowR = row[c+1:]
			row = currRowL + col.pop(0) + currRowR
			
			dish.pop(i)
			dish.insert(i, row)

#################################
input = IN[0]

cycle = 0		# current cycle 
cycles =  1	# count of cycles to run through
dish = []		# current arrangement of rocks on dish
load = 0		# SOLUTION | sum of loads of rocks on dish
#################################

# set up dish with starting position of rocks
for line in input:
	dish.append(line.strip())

# run through each tilt maneuver || PART1 only north tilt
while cycle < cycles:
	# tilt north
	for i in range(1,len(dish)):
		TiltNS(i, "north")
		
	# tilt west
#	for i in range(1, len(dish[0])):
#		TiltWE(i, "west")
		
	# tilt south
#	for j in range(2, len(dish)+1):
#		i = len(dish) - j
#		TiltNS(i, "south")
		
	# tilt east
#	for j in range(2, len(dish)+1):
#		i = len(dish) - j
#		TiltWE(i, "east")
	
	cycle += 1

# sum up load of rocks based on row position (row 0 = len(dish), row 1 = len(dish)-1,...)
for i in range(0, len(dish)):
	score = len(dish) - i
	rocksInRow = 0
	for obj in dish[i]:
		if obj == "O":
			rocksInRow += 1
	load += rocksInRow * score

OUT = input, dish, load
