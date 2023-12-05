import sys
import clr
clr.AddReference('ProtoGeometry')

def Convert (group, name):
	# from the input, create conversion ruleset for each group
	sourceStart = int(group.split(" ")[1].strip())
	destStart = int(group.split(" ")[0].strip())
	length = int(group.split(" ")[2].strip())
	
	# get end of source range and the conversion (delta between source and destination)
	sourceEnd = sourceStart + length - 1
	delta = destStart - sourceStart
	conversion = "%s,%s,%s" %(sourceStart, sourceEnd, delta)
	
	# add the ruleset range to the corresponding set
	if name == "seed":
		soils1.add(conversion)
	elif name == "soil":
		ferts1.add(conversion)
	elif name == "fertilizer":
		waters1.add(conversion)
	elif name == "water":
		lights1.add(conversion)
	elif name == "light":
		temps1.add(conversion)
	elif name == "temperature":
		humids1.add(conversion)
	elif name == "humidity":
		locs1.add(conversion)


def LookFor (curr, list):
	# PART 1 | run through each dict and look for corresponding value
	# see if current seed lies within a ruleset range
	found = 0
	for line in list:
		if found == 0:
			start = int(line.split(",")[0])
			end = int(line.split(",")[1])
			
			# if found a corresponding ruleset, convert the seed
			if curr >= start and curr <= end:
				found += 1
				delta = int(line.split(",")[2])
				curr += delta
	return curr


def LookFor2 (curr, list):
	# PART 2 | run through each dict and look for corresponding value
	newRanges = ""		# string to store ranges for the next iteration
	currRanges = []		# list to store current ranges to look for
	# set up currRanges list
	if "," in curr:
		currRanges = curr.split(",")
	elif curr == []:
		for range in curr:
			currRanges.append(range)
	else:
		currRanges.append(curr)
	
	# run through each range in currRanges list and look for corresponding rulesets
	while len(currRanges) > 0:
		range = currRanges.pop(0)
		found = 0				# int to track if found matching range
		partial = 0				# int to track if split ranges
		tempRanges = set()		# set to store found / split ranges
		
		# get the start and end of the current range
		rangeStart = -2
		rangeEnd = -1
		if ".." in range:		# if range has 2 nums
			rangeStart = int(range.split("..")[0])
			rangeEnd = int(range.split("..")[1])
		else:		# if range has 1 num
			rangeStart = int(range)
			rangeEnd = rangeStart
		
		# if current range has unique start and end, look for matching ruleset
		if rangeStart != rangeEnd and rangeStart != -2 and rangeEnd != -1:
			for line in list:
				if found == 0:
					start = int(line.split(",")[0])		# start of ruleset
					end = int(line.split(",")[1])		# end of ruleset
					newRange = ""		# string for new found range
					splitRange1 = ""	# string for split range 1, if applicable
					splitRange2 = ""	# string for split range 2, if applicable
					
					# if both range start and end in ruleset's range, calc new range
					if rangeStart >= start and rangeEnd <= end:
						found += 1
						delta = int(line.split(",")[2])
						newStart = rangeStart + delta
						newEnd = rangeEnd + delta
						newRange = "%s..%s," %(newStart, newEnd)
					
					# if just the start in the ruleset's range, split up into 2 ranges
					elif rangeStart >= start and rangeStart <= end:
						partial += 1
						if rangeStart != end:
							splitRange1 = "%s..%s" %(rangeStart, end)
							splitRange2 = "%s..%s" %(end+1, rangeEnd)
						else:
							splitRange1 = "%s..%s" %(rangeStart, rangeStart)
							SplitRange2 = "%s..%s" %(rangeStart+1, rangeEnd)
					
					# if just the end in the ruleset's range, split up into 2 ranges
					elif rangeEnd >= start and rangeEnd <= end:
						partial += 1
						if rangeEnd != start:
							splitRange1 = "%s..%s" %(rangeStart, start-1)
							splitRange2 = "%s..%s" %(start, rangeEnd)
						else:
							splitRange1 = "%s..%s" %(rangeEnd, rangeEnd)
							splitRange2 = "%s..%s" %(rangeStart, rangeEnd-1)
					
					# if found the new range, add to the list
					if newRange != "":
						newRanges += newRange
					
					# if found split ranges, add to the temp set
					if splitRange1 != "" and splitRange2 != "":
						tempRanges.add(splitRange1)
						tempRanges.add(splitRange2)
		
		# if the range is just one number, see if it lies in a ruleset
		elif rangeStart == rangeEnd:
			for line in list:
				if found == 0:
					start = int(line.split(",")[0])
					end = int(line.split(",")[1])
					newRange = ""
					
					# see if the range is the start or end of a ruleset
					if rangeStart == start:
						delta = int(line.split(",")[2])
						newStart = rangeStart + delta
						newRange = "%s..%s," %(newStart, newStart)
					elif rangeEnd == end:
						delta = int(line.split(",")[2])
						newEnd = rangeEnd + delta
						newRange = "%s..%s," %(newEnd, newEnd)
					
					# if modified, add revision to the list
					if newRange != "":
						found += 1
						newRanges += newRange
		
		# if no applicable range, keep the range for the next LookFor2()
		if found == 0 and partial == 0:
			newRanges += "%s," %range
		
		# if found split ranges, add them to the currRanges to look for corresponding rulesets
		elif partial > 0:
			for tempRange in tempRanges:
				currRanges.append(tempRange)
	
	# move new list of ranges to next iteration
	newRanges = newRanges[:-1]	
	return newRanges

###################################
input = IN[0]

# SEEDS -> SOILS -> FERTILIZERS -> WATERS -> LIGHTS -> TEMPERATURES -> HUMIDITYS -> LOCATIONS
seeds = []			# list of seeds
soils1 = set()		# set to store soils conversion rules
ferts1 = set()		# set to store fertilizer conversion rules
waters1 = set()		# set to store water conversion rules
lights1 = set()		# set to store light conversion rules
temps1 = set()		# set to store temperature conversion rules
humids1 = set()		# set to store humidity conversion rules
locs1 = set()		# set to store locations conversion rules

lowest1 = -1		# SOLUTION PART 1 | find lowest number location out of all seeds
lowest2 = -1		# SOLUTION PART 2 | find lowest number location
###################################

# splut up input into various lists
curr = ""
for line in input:
	if line[0] in ["s","f","w","l","t","h"]:
		curr = line
		if curr[0:5] == "seeds":
			seeds = curr.split(": ")[1].split(" ")
	else:
		first = curr.split("-")[0]
		convert = Convert(line, first)

# --- PART 1 ---------------
# for each seed, run through the various conversions
for seed in seeds:
	seed = int(seed)

	loc = LookFor (LookFor (LookFor (LookFor (LookFor (LookFor (LookFor(
			seed, soils1), ferts1), waters1), lights1), temps1), humids1), locs1)
	
	# look for the lowest location value
	if loc < lowest1 or lowest1 == -1:
		lowest1 = loc

# --- PART 2 ---------------
# combine seeds into pairs of ranges (seed1..seed2 = min..max)
seedRanges = []
pairs = []
for seed in seeds:
	pairs.append(seed)
	if len(pairs) == 2:
		a = int(pairs[0])
		b = a + int(pairs[1]) - 1
		seedRanges.append("%s..%s" %(a,b))
		pairs = []

# for each range of seeds, run through the various conversions
for seedRange in seedRanges:
	loc = LookFor2 (LookFor2 (LookFor2 (LookFor2 (LookFor2 (LookFor2 (LookFor2 (
			seedRange, soils1), ferts1), waters1), lights1), temps1), humids1), locs1)
	
	# check each range of locations for the lowest value
	for range in loc.split(","):
		start = int(range.split("..")[0])
		if start < lowest2 or lowest2 == -1:
			lowest2 = start
	

OUT = lowest1, lowest2
