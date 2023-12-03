import clr
clr.AddReference('ProtoGeometry')

def GetNeighbors (part, row, col):
	# determine if parts are valid by their neighbors (e.g. &,*,$)
	# also collect the neighbors of gears (*)
	
	# set up min/max row for the current part
	rowMin = row - 1
	if rowMin < 0:
		rowMin = 0
	rowMax = row + 1
	if rowMax > lastRow:
		rowMax = lastRow
	
	# set up min/max col for the current part
	colMin = col - len(part) - 1
	if colMin < 0:
		colMin = 0
	colMax = col
	if colMax > lastCol:
		colMax = lastCol
	
	# determine if part is valid if it has a symbol adjacent to it
	valid = False
	for r in range(rowMin, rowMax+1):
		for c in range(colMin, colMax+1):
			char = input[r][c]
			
			# if has a symbol, the part is valid
			if char not in nums and char != ".":
				valid = True
				
				# PART 2: if the symbol is a (*) it's a gear
				if char == "*":
					pos = "%s,%s" %(r,c)
					
					# add the gear to the dictionary and store the neighboring part
					if pos not in gears.keys():
						gears[pos] = [part]
					else:
						partList = gears[pos]
						partList.append(part)
						gears[pos] = partList
	
	return valid

################################
input = IN[0]

nums = ["0","1","2","3","4","5","6","7","8","9"]	# list of nums as strings
lastRow = len(input) -1			  # last row in input
lastCol = len(input[0]) -1		# last col in input

validParts = []		# list to store valid parts
invalidParts = []	# list to store invalid parts
partSum = 0			  # PART 1: sum of valid parts

gears = {}		  	# PART 2: dict of gears 
gearSum = 0		  	# PART 2: sum of gear ratios
################################

# run through each line in input looking for part numbers
for i in range(0, len(input)):
	row = input[i]
	part = ""
	for j in range(0, len(row)):
		char = row[j]
		
		# if a number, collect until end of number, en dof row, or adjacent symbol
		if char in nums:
			part += char
		if char not in nums or j == len(row)-1:
			# determine validity of the part by checking its neighbors
			if part != "":
				isValid = GetNeighbors(part, i, j)
				if isValid == True:
					validParts.append(part)
					partSum += int(part)		# PART 1: sum up valid part numbers
				else:
					invalidParts.append(part)
				
				part = ""
		
		# PART 2: if character is a gear (*) add it to the dictionary
		if char == "*":
			pos = "%s,%s" %(i,j)
			if pos not in gears.keys():
				gears[pos] = []

# PART 2: get the gear ratio for valid gears
for gear in gears.keys():
	count = gears[gear]
	
	# for gears with exactly 2 parts, multiply the part nums to get ratio
	if len(count) == 2:
		gearRatio = 1
		debug.append("(%s): " %gear)
		for part in count:
			gearRatio *= int(part)
		
		# sum the gear ratios
		gearSum += gearRatio

OUT = partSum, gearSum, invalidParts
