import sys
import clr
clr.AddReference('ProtoGeometry')
import math

#################################
input = IN[0]
times = []		# list of times from input
dists = []		# list of distances from input
margin = 1		# PART 1 SOLUTION | multiply possible ways together
margin2 = 0		# PART 2 SOLUTION | difference between parabola roots
debug = []
#################################

#-- PART 1 --------------------
# split up input into times and dists lists
inputTime = input[0].split(" ")[1:]
inputDist = input[1].split(" ")[1:]
for time in inputTime:
	if time != "":
		times.append(int(time.strip()))
for dist in inputDist:
	if dist != "":
		dists.append(int(dist.strip()))

# run through each time/dist pair to 
for i in range(0, len(times)):
	time = times[i]
	dist = dists[i]
	
	# beginning at time t=0, find the first half of winning times
	t = 0
	winners = 0
	while t <= time//2:
		if (t * (time - t)) > dist:
			winners += 1
		t += 1
	
	# multiply by 2 to get whole set, and subtract 1 for even times
	winners *= 2
	mod = time % 2
	if mod == 0:
		winners -= 1
		
	# multiply margin (solution) by winning count 
	margin *= winners

#-- PART 2 -------------
# concatenate times and distances to get actual time and dist
time2 = int(input[0].split(":")[1].replace(" ", ""))
dist2 = int(input[1].split(":")[1].replace(" ", ""))

# use the quadratic formula to solve for the roots of the parabola
quad = ((time2**2) - (4 * dist2))**0.5
x1 = ( (time2 + quad)/2 ) // 1 + 1
x2 = ( (time2 - quad)/2 ) // 1 + 1
debug.append([x1, x2])
margin2 = abs(x2 - x1)

# alternative quadratic formula solution:
x1 = int((time2 + math.sqrt(pow(time2, 2) - 4 * dist2))/2)
x2 = int((time2 - math.sqrt(pow(time2, 2) - 4 * dist2))/2)
delta = x1 - x2

OUT = margin, margin2, debug
