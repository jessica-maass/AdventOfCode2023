import sys
import clr
clr.AddReference('ProtoGeometry')

def GetMirrorAxis (field):
	# for each mirror field, look for horiz or vert lines of mirror
	rows = {}		# dict of rows in field
	cols = {}		# dict of cols in field
	
	axisR = []		# list of possible mirror lines for row
	axisC = []		# list of possible mirror lines for col
	mirrorR = 0		# index of mirror line for row
	mirrorC = 0		# index of mirror line for col
	
	# create list of rows to check
	for r in range(0, len(field)):
		rows[r] = field[r]
	rowMax = len(rows.keys())
	
	# run through each row looking for possible mirror matches
	for r1 in range(0, rowMax):
		row1 = rows[r1]
		for r2 in range(0, rowMax):
			if r1 != r2:
				row2 = rows[r2]
				if row1 == row2:
					a = min(r1, r2) + 1
					b = max(r1, r2) + 1
					
					# if found possible mirror, copy to list
					if b - a == 1 and a not in axisR:
						axisR.append(a)
	
	# if possible mirrors, go through each and see if valid
	if len(axisR) > 0:
		while len(axisR) > 0:
			axis = axisR.pop(0)
			rows1 = field[0:axis]
			rows2 = field[axis:]
			
			# for the current possible axis, see if valid mirroring
			mirrored = True
			if len(rows1) > 0 and len(rows2) > 0:
				while len(rows1) > 0 and len(rows2) > 0:
					row1 = rows1.pop()
					row2 = rows2.pop(0)
					
					# if mirrored rows don't match, axis is not valid
					if row1 != row2:
						mirrored = False
						break
			
			# if all rows mirrored, the axis is valid mirror line
			if mirrored == True:
				mirrorR = axis
				break

	# collect each column of the mirror
	for c in range(0, len(rows[0])):
		cols[c] = ""
	for i in range(0, rowMax):
		for j in range(0, len(rows[0])):
			cols[j] += rows[i][j]
	colMax = len(cols.keys())
	
	# run through each col looking for possible mirror matches
	for c1 in range(0, colMax):
		col1 = cols[c1]
		for c2 in range(0, colMax):
			if c1 != c2:
				col2 = cols[c2]
				if col1 == col2:
					a = min(c1, c2) + 1
					b = max(c1, c2) + 1
					
					# if found possible mirror, copy to list
					if b-a == 1 and a not in axisC:
						axisC.append(a)
	
	# if possible mirrors, go through each and see if valid
	if len(axisC) > 0:
		while len(axisC) > 0:
			axis = axisC.pop(0)
			cols1 = []
			cols2 = []
			for i in range(0, axis):
				cols1.append(cols[i])
			for i in range(axis, colMax):
				cols2.append(cols[i])
			
			# for the current possible axis, see if valid mirroring
			mirrored = True
			if len(cols1) > 0 and len(cols2) > 0:
				while len(cols1) > 0 and len(cols2) > 0:
					col1 = cols1.pop()
					col2 = cols2.pop(0)
					
					# if mirrored cols don't match, axis is not valid
					if col1 != col2:
						mirrored = False
						break
			
			# if all cols mirrored, the axis is valid mirror line
			if mirrored == True:
				debug.append("--> C @ %s" %axis)
				mirrorC = axis
				break
	
	if mirrorC == 0:
		debug.append("--> No C mirror")
	
	return mirrorR, mirrorC, otherR, otherC

#################################
input = IN[0]

fields = []			# list of mirrors
mirrorLines = []	# list of found horiz/vert mirror lines
sums = 0			# SOLUTION | sum of rows/cols above/left of mirror lines
#################################

# split up input 
temp = ""
for line in input.split("\n"):
	if "." not in line and "#" not in line:
		temp += "X"
	else:
		temp += line.strip() + ","

# run through each mirror in input
for field in temp.split("X"):
	f = field.split(",")[:-1]
	fields.append(f)
	
	# get vert/horiz mirror lines
	axes = GetMirrorAxis (f)
	axisHoriz = axes[0]
	axisVert = axes[1]
	mirrorLines.append("H: %s | V: %s" %(axisHoriz, axisVert))
	
	# sum cols/rows above/right of mirror line
	sum = axisVert + (100 * axisHoriz)
	sums += sum

OUT = sums, mirrorLines
