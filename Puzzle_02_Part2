# Created in Dynamo 1.2.2.373
import clr
clr.AddReference('ProtoGeometry')

#################################
input = IN[0]

powers = []		# list of power of each min set of cubes
sum = 0			# sum of powers
#################################

# run through each game to determine min possible cubes
for line in input:
	id = line.split(":")[0][5:]
	rounds = line.split(": ")[1].split("; ")
	
	# initialize the minimum cube dictionary for the game
	minCubes = {"red":0, "green":0, "blue":0}
	
	# run through each round in game
	for round in rounds:
		draws = round.split(", ")
		
		# for each draw in round, get the count of each cube color
		for draw in draws:
			count = int(draw.split(" ")[0])
			color = draw.split(" ")[1]
			
			# if the current draw color count is bigger, increase the dictionary
			if minCubes[color] == 0 or minCubes[color] < count:
				minCubes[color] = count
	
	# get min counts and determine the power (r*g*b)
	red = minCubes["red"]
	green = minCubes["green"]
	blue = minCubes["blue"]
	power = red * green * blue
	powers.append(power)
	sum += power

OUT = sum, powers
