import sys
import clr
clr.AddReference('ProtoGeometry')
from itertools import combinations	# MVP of the problem!!!

def GetArrangements (spring, group):
	# given the line, determine all possible arrangements of springs
	possible = 0		# count of possible groupings of valid springs
	
	damageTotal = 0		# total number of damaged springs in row
	for g in group.split(","):
		damageTotal += int(g)
	
	known = 0		# count of all known damaged springs ("#" in string)
	unknown = 0		# count of all unknown springs ("?" in string)
	missing = 0		# count of unknown damaged springs (total - known)
	for s in spring:
		if s == "#":
			known += 1
		elif s == "?":
			unknown += 1
	missing = damageTotal - known
	
	# if unknown springs = missing springs, only one possibility
	if unknown == missing:
		possible = 1
	
	# otherwise run through all possible groupings and find valid possible ones
	else:
		# get index positions of unknown locations
		posUnknown = []
		for s in range(0, len(spring)):
			if spring[s] == "?":
				posUnknown.append(s)
		
		# create groups of N (where N = missing) from total unknown positions
		# e.g. unknown of [0,1,2] with 2 missing = [0,1], [0,2], [1,2]
		combos = list(combinations(posUnknown,missing))
		
		# for each groups of N, reaplce missing (?) with either damaged (#) or undamaged (.) spring
		for combo in combos:
			newSpring = ""
			for i in range(0, len(spring)):
				s = spring[i]
				if i in combo:
					newSpring += "#"
				elif s == "?":
					newSpring += "."
				else:
					newSpring += s
			
			# for each new spring, group the damaged springs together (e.g. 1,1,3)
			newGroup = ""
			for g in newSpring.Split("."):
				if g != "":
					count = 0
					for char in g:
						if char == "#":
							count += 1
					newGroup += "%s," %count
			newGroup = newGroup[:-1]
			
			# compare old and new groupings to see if match 
			if group.split(",") == newGroup.split(","):
				possible += 1
	
	return possible

#################################
input = IN[0]

possibilities = []	# list of valid possible counts for each spring row
possibleSum = 0		# PART 1 | sum of valid counts for each spring row

debug = []
#################################
# for each spring row, determine possibble variations of damaged/undamaged springs
for line in input:
	spring = line.split(" ")[0]
	group = line.split(" ")[1]
	possibilities.append(GetArrangements (spring, group))

# sum up all possibilities
for possible in possibilities:
	possibleSum += possible

OUT = possibleSum, possibilities
