import sys
import clr

###########################
input = IN[0]
lettersIn = IN[1]

letters = set()		# set of letters a thru z
calibration = []	# list of nums found in input
value = 0			# solution; sum of nums

debug = []
###########################

# create set from input list of a thru z
for letter in lettersIn:
	letters.add(letter)

# run through input and collect first and last num
while len(input) > 0:
	line = input.pop(0)
	digits = ""
	
	# for each char in line collect only nums
	for char in line:
		if char not in letters:
			digits += char
	
	# determine first and last. if only 1 num it's both
	if len(digits) == 1:
		digits += digits
	if len(digits) > 2:
		digits = digits[0] + digits[-1]
	
	# sum up found nums
	if len(digits) == 2:
		calibration.append(int(digits))
		value += int(digits)

OUT = value, calibration
