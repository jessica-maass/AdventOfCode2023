import sys
import clr
clr.AddReference('ProtoGeometry')

##################################
input = IN[0]

winPoints = []		# PART 1 | list to store winning point values
total = 0			# PART 1 | sum of winning card point values

cardCounts = {}		# PART 2 | dict to store totals of each card used/won
cardTotal = 0		# PART 2 | sum of all cards scratched incl copies
##################################

# find matching numbers in each card, and calc winning score
for card in input:
	
	# PART 2: initialize cardCount dict
	cardNum = int(card.split(": ")[0][5:].strip())
	if cardNum not in cardCounts.keys():
		cardCounts[cardNum] = 0
	cardCounts[cardNum] += 1
	
	# split up input into winning nums and have nums
	nums = card.split(": ")[1]
	winningNums = nums.split(" | ")[0].split(" ")
	haveNums = nums.split(" | ")[1].split(" ")
	
	# create set of winners
	winners = set()
	for winning in winningNums:
		if winning != "":
			winners.add(winning)
	
	# count up how many matches there are
	matches = 0
	for have in haveNums:
		if have in winners:
			matches += 1
	
	# PART 1: if found matches, get score as 2 to the power of X-1
	if matches > 0:
		score = 2**(matches-1)
		winPoints.append(score)
		total += score
	else:
		winPoints.append(0)
	
	# PART 2: each match gets copy of next successive cards
	for i in range(0, matches):
		# get next card numers (e.g. if curr card is 1, get 2, 3, 4, etc)
		copy = i + cardNum + 1
		
		# add card to dict if not already there
		if copy not in cardCounts.keys():
			cardCounts[copy] = 0
		
		# add copies of the cards
		cardCounts[copy] += cardCounts[cardNum]

# PART 2 solution: sum up total of all cards
for card in cardCounts.keys():
	cardTotal += cardCounts[card]
	
# visualize the dictionary
counts = []
for i in range(0, len(cardCounts)):
	counts.append("#%s : %s" %(i+1, cardCounts[i+1]))
	

OUT = total, cardTotal, counts
