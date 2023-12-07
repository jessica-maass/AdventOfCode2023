import sys
import clr

def GetValue(num):
	# get value of string number as int
	val = -1
	if num in integers:
		val = int(num)
	elif num in written:
		val = writDict[num]
	return val

def LengthOne (item):
	# if only one string found, get its value
	val = -1
	num = item.split("]")[1]
	num = str(GetValue(num))
	if len(num) == 1:
		val = int(num+num)
	else:
		val = int(num)
	return val

def LengthTwo (item1, item2):
	# if two strings found, determine if unique or duplicate; then get value
	val = ""							# value of num to find
	int1 = int(item1.split("]")[0])		# first int from strings
	int2 = int(item2.split("]")[0])		# second int from strings
	num1 = item1.split("]")[1]			# first num from strings
	num2 = item2.split("]")[1]			# second num from strings
	
	# if two unique digits, get both values
	if int1 != int2:
		j = [0,1]
		if int1 > int2:
			j = [1,0]
		nums = [str(GetValue(num1)), str(GetValue(num2))]
		val = "%s%s" %(nums[j[0]], nums[j[1]])
	
	# if only one digit, get its value
	if int1 == int2:
		debug.append("1 num")
		val = str(LengthOne(item2))
	
	# if result has more than 2 digits, only save first and last
	if len(val) > 2:
		val = int(val[0] + val[-1])
	
	return val

def LengthThree (items):
	# if more than two strings, get the first and last; then get value
	val = ""	# value of nums to find
	ints = []	# list of ints from strings
	nums = []	# list of nums from strings
	
	# for each item in input, collec the ints and nums
	for item in items:
		ints.append(int(item.split("]")[0]))
		nums.append(item.split("]")[1])
	
	# count how many are unique
	uniqueInts = set()
	for i in ints:
		uniqueInts.add(i)
	
	# if multiple unique ints, 
	if len(uniqueInts) > 1:
		if len(ints) == len(uniqueInts):
			i0 = ints.IndexOf(min(ints))
			i1 = ints.IndexOf(max(ints))
			
			# get the value of the digits
			val = LengthTwo(items[i0], items[i1])
	
	return val

#########################################
input = IN[0]

integers = set()	# set of all integers 0->9 as strings
written = set()		# set of numbers written out as strings, e.g. "one"
writDict = {}		# dictionary to correspond written nums with actual nums
calibration = []	# list to collect digits found in input
value = 0			# SOLUTION | sum of digits

# create set of letters to search for
for i in [0,1,2,3,4,5,6,7,8,9]:
	integers.add(str(i))

# create sets and dictionary of written numbers and corresponding value
singles = ["one","two","three","four","five","six","seven","eight","nine"]
singlesNum = [1,2,3,4,5,6,7,8,9]
unique = ["zero", "eleven","twelve","thirteen","fourteen",
		  "fifteen","sixteen","seventeen","eighteen","nineteen"]
uniqueNum = [0,11,12,13,14,15,16,17,18,19]
tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
tensNum = [10,20,30,40,50,60,70,80,90]

#############################################

# set up the writDict dictionary
for i in range(0,10):
	# add the unique nums, e.g. eleven, fifteen
	num = unique[i]
	writDict[num] = uniqueNum[i]
	
	# add the tens nums, e.g. twenty, thirty
	if i < 9:
		ten = tens[i]
		#written.add(ten)
		writDict[ten] = tensNum[i]
		
		# add the singles e.g. one, four,, and combo nums, e.g twentyfour, fiftysix
		if ten != "ten":
			for j in range(0,9):
				single = singles[j]
				writDict[single] = singlesNum[j]
				
				num = ten+single
				writDict[num] = writDict[ten] + writDict[single]

# set up the written set
for key in writDict.keys():
	written.add(key)

# visualize the dictionary
vis = []
for key in writDict.keys():
	val = writDict[key]
	vis.append("%s | %s" %(val, key))

# run through each line in input looking for non-letter characters
while len(input) > 0:
	line = input.pop(0)
	found = []

	# collect the string numbers from the line using windows
	window = ""
	for i in range(0, len(line)):
		# first collect the num if it's an int (e.g. 1, 3, 5)
		char = line[i]
		if char in integers:
			found.append("%s]%s" %(i, char))
		
		# for written nums, get all possible nums in each window
		temps = []		# store the written nums found
		end = 13		# size of window based on longest written num length)
		count = 1+len(line)-i	# truncate window as get closer to the end
		if count <= end:
			end = count
		
		# search the line for written nums
		for size in range(3,end):
			window = line[i:i+size]
			if window in written:
				temps.append("%s]%s" %(i,window))
			
			# at end of window, see if found any written nums
			if size == end-1 and len(temps) > 0:
				
				# get the last if multiple (e.g. sixtyone = six, sixty, sixtyone)
				new = temps[0]
				if len(temps) > 1:
					new = temps[-1]
				
				# if first found number, just add it to list
				if len(found) == 0:
					found.append(new)
				
				# else compare it with last found num and see if unique
				else:
					last = found[-1]
					intX = int(last.split("]")[0])
					numX = last.split("]")[1]
					
					# if the previous is an integer, then new written is unique
					if numX in integers:
						found.append(new)
					
					# otherwise, see if the new number is part of the previously found written num
					else:
						int0 = int(new.split("]")[0])
						num0 = new.split("]")[1]
						if num0 != numX[-len(num0):]:	# is the new num part of previous (e.g. twentyone and one)
							if int0 != intX + len(numX) - len(num0):	# is the new int part of the previous
								found.append(new)
	
	# for the found numbers, find the first/last value
	digits = ""
	if len(found) == 1:
		digits = LengthOne(found[0])
	elif len(found) == 2:
		digits = LengthTwo(found[0], found[1])
	elif len(found) >= 3:
		digits = LengthThree(found)
	
	# sum up the solutions
	calibration.append("%s | %s" %(digits, line))
	add = int(calibration[-1].split(" | ")[0])
	value += add

OUT = value, calibration
