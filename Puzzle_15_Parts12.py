import sys
import clr
clr.AddReference('ProtoGeometry')
import string

def Hash (str, operator = "", focal = 0):
	# run the HASH algorithm on the character
	val = 0
	for char in str:
		val += ascii[char]
		val *= 17
		val = val % 256
	
	# PART 1 | return the value
	if operator == "":
		return val
	
	# PART 2 | move to the next step
	else:
		Hashmap (str, val, op, focal)

def Hashmap (label, box, operator, focal):
	# for the given lens, see if need to add or remove from given box
	curr = boxes[box]
	
	# get current lens and their focal lengths for the box
	currLens = []
	currFocal = []
	for lens in curr:
		currLens.append(lens.split(",")[0])
		currFocal.append(lens.split(",")[1])
	
	# remove the given lens from the box, if it's in there
	if operator == "-":
		if label in currLens:
			i = currLens.IndexOf(label)
			curr.pop(i)
	
	# add the given lens to the box
	elif operator == "=":
		# if the lens label not in the box, add it to the end of the list
		if label not in currLens:
			curr.append("%s,%s" %(label, focal))
		
		# if the lens is in the box, update the focal length with the given focal
		elif label in currLens:
			i = currLens.IndexOf(label)
			curr.pop(i)
			curr.insert(i, "%s,%s" %(label, focal))
		
		# if the focal length is in the box, replace the label with the given lens
		elif focal in currFocal:
			i = currFocal.IndexOf(focal)
			curr.pop(i)
			curr.insert(i, "%s,%s" %(label, focal))
	
	# update the box's list
	boxes[box] = curr

#################################
input = IN[0]

ascii = {}		# dict of ascii characters and corresponding number
boxes = {}		# dict of boxes and the lenses in them

sum = 0			# PART 1 | sum of results of sequences thru HASH
power = 0		# PART 2 | sum of lens in boxes based on position
#################################

# set up dict of ascii characters
asciiList = map(chr, range(33, 127))
for i in range(33, 127):
	j = i - 33
	ascii[asciiList[j]] = i

# create dict of boxes
for b in range(0, 256):
	boxes[b] = []

# PART 1 | run each sequence in input through HASH and sum up final values
for seq in input.split(","):
	s = seq.strip()
	value = Hash (s)
	sum += value
	
# PART 2 | with each sequence's label and operator, add/remove to found box
	# split up the sequence into operator, label, and focal length
	op = ""
	label = ""
	focalLength = 0
	if "=" in s:
		op = "="
		split = s.split("=")
		label = split[0].strip()
		
		if split[1].strip() != "":
			focalLength = split[1].strip()
	elif "-" in s:
		op = "-"
		label = s.split("-")[0].strip()
	
	# run through HASH to get box number
	Hash(label, op, focalLength)

# calculate the power in each box
for box in range(0, 256):
	if boxes[box] != []:
		value = 0
		for i in range(0, len(boxes[box])):
			lens = boxes[box][i].split(",")[0]
			focal = int(boxes[box][i].split(",")[1])
			pow = (box + 1) * (i + 1) * focal
			
			# add the current box power to the final power
			power += pow

OUT = sum, power
