# Craete in Dynamo 1.2.2.373
import clr
clr.AddReference('ProtoGeometry')

#################################
input = IN[0]

redMax = 12		# max num of red cubs in bag
greenMax = 13	# max num of green cubes in bag
blueMax = 14	# max num of blue cubes in bag
colorMax = {"red":redMax, "green":greenMax, "blue":blueMax}	# dict to store color mins

possible = []	# list of valid game ID's
sum = 0			# sum of valid game ID's
#################################

# run through each game and check cube counts for validity
for line in input:
	id = line.split(":")[0][5:]
	rounds = line.split(": ")[1].split("; ")
	
	# run through each round in game
	validRounds = 0
	for round in rounds:
		draws = round.split(", ")
		
		# for each draw in round, get cube count for each color
		validDraws = 0
		for draw in draws:
			count = int(draw.split(" ")[0])
			color = draw.split(" ")[1]
			
			# compare draw's cube count to the min cube count
			if count <= colorMax[color]:
				validDraws += 1
		
		# if all draws are valid, the round is valid
		if validDraws == len(draws):
			validRounds += 1
	
	# if all rounds are valid, collect the game ID
	if validRounds == len(rounds):
		possible.append(id)
		sum += int(id)
			
OUT = sum, possible
