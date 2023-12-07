import sys
import clr
clr.AddReference('ProtoGeometry')

def GetType (hand):
	# given the 5-card hand, determine its type (e.g. full house, two pair)
	type = ""	# type of hand
	cards = {}	# individual cards and counts
	joker = 0	# track if joker present "J"
	
	# for each card in hand, collect which ones and how many e.g. 1 Q and 4 K
	for card in hand:
		if card not in cards.keys():
			cards[card] = 0
		cards[card] += 1
		if card == "J":
			joker += 1
	
	# get unique card values and use that to determine hand type
	unique = len(cards.keys())
	if unique == 1:						# five of a kind
		type = "five"
	elif unique == 2:					# four of a kind or full house
		vals = cards.values()
		if 4 in vals and 1 in vals:
			type = "four"
		elif 3 in vals and 2 in vals:
			type = "full"
	elif unique == 3:					# three of a kind or two pair
		vals = cards.values()
		if 3 in vals:
			type = "three"
		elif 2 in vals:
			type = "two"
	elif unique == 4:					# one pair
		type = "one"
	elif unique == 5:					# high card
		type = "high"
	
	# PART 2 | if the hand has a J (joker), modify the type
	if joker > 0:
		if unique == 2:						# OG: four of a kind or full house
			type = "five"
		elif unique == 3:					# OG: three of a kind or two pair
			if joker == 1:
				if 3 in cards.values():
					type = "four"
				else:
					type = "full"
			elif joker == 2 or joker == 3:
				type = "four"
		elif unique == 4:					# OG: one pair
			if joker == 1:
				type = "three"
			elif joker == 2:
				type = "three"
		elif unique == 5:					# OG: high card
			type = "one"
	
	# collect list of hands by type, store in dictionary
	if type not in groups.keys():
		groups[type] = [hand]
	else:
		groupList = groups[type]
		groupList.append(hand)
		groups[type] = groupList
	
	# get the score for each card in this hand, store in dictionary
	score = ""
	for card in hand:
		for v in range(0, len(values)):
			if values[v] == card:
				score += "%s," %v
	scores[hand] = score
	
	return type

def CompareHands (handList, type, n = 1):
	# compare multiple hands of the same type and order them
	order = []		# list of hands ordered from lowest to highest rank
	found = set()	# set to track hands already ordered
	
	# run through each hand startig from first card, and compare value of the card
	v = 0
	while v < len(values):
		# run through each hand and collect them if nth carad has value v
		compare = []
		for hand in handList:
			score = scores[hand].split(",")
			
			# if hand's nth card is v, collect it and mark hand as found
			if int(score[n-1]) == v and hand not in found:
				compare.append(hand)
				found.add(hand)
		
		# if found hands with value v at nth card:
		if compare != []:
			s = values[v]
			# if only one card, at to the order list
			if len(compare) == 1:
				order.append(compare[0])
			
			# else multiple cards, iterate to the next nth card 
			else:
				subSort = CompareHands (compare, type, n+1)
				for card in subSort:
					order.append(card)
		v += 1
	
	return order

#################################
input = IN[0]

values1 = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]	# values for PART 1
values2 = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]	# values for PART 2
values  = values2	# values to use in code
types = ["five","four","full","three","two","one","high"]	# types of hands
groups = {}		# dict to store hands for each type
hands = {}		# dict to store type for each hand
scores = {}		# dict to store score for each hand
ranks = {}		# dict to store rank for each hand
currRank = 1	# int to count current ranking
bids = {}		# dict to store bid for each hand
winnings = 0	# SOLUTION | sum up the total winnings
#################################
# organize values by lowest -> greatest
values.reverse()

# split up input and initialize dictionaries
for line in input:
	hand = line.split(" ")[0]
	bid = line.split(" ")[1]
	hands[hand] = GetType(hand)
	ranks[hand] = -1
	bids[hand] = int(bid)

# rank the hands by their type then by their strength
for i in range(0, len(types)):
	j = -1 - i
	type = types[j]
	
	# if the type (e.g. two pair) is in the input hands, sort them
	if type in groups.keys():
		
		# if multiple hands of the type, sort them
		if len(groups[type]) > 1:
			sorted = CompareHands (groups[type], type)
			
			# with sorted list of hands, rank and add the winnings
			for hand in sorted:
				ranks[hand] = currRank
				winnings += currRank * bids[hand]	
				currRank += 1
		
		# if only one hand of type, immediately rank
		else:
			hand = groups[type][0]
			ranks[hand] = currRank
			
			# add the winnings and increment the currRank
			winnings += currRank * bids[hand]
			currRank += 1

OUT = winnings
