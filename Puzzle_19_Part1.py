def Sort (part, rule = "in"):
	# for each part, run through rules and determine next step
	result = ""
	
	# create dict of the part's x,m,a,s rating values
	ratings = {}
	for r in part.split(","):
		name = r.split("=")[0]
		val = int(r.split("=")[1])
		ratings[name] = val
	
	# start with rule "in", then go from there
	workflow = rules[rule].split(",")
	ifThis = rules[rule].split(",")[0]
	leftover = rules[rule].split(",")[1:]
	
	# run through the rules of the workflow until get result
	while len(workflow) > 0 and result == "":
		next = workflow.pop(0)
		left = []
		if len(workflow) > 0:
			for work in workflow:
				left.append(work)
		
		# if not the last item, check the comparison to see wheter to use true or false
		if left != []:
			op = next[1]
			rating = ratings[next[0]]
			check = int(next.split(":")[0][2:])
			ifTrue = next.split(":")[1]
			ifFalse = "X"
			if len(left) > 0:
				ifFalse = left.pop(0)
			next = Compare (op, rating, check, ifTrue, ifFalse)
		
		# if found the end result, return it		
		if next == "A":
			result = "A"
			return result
		elif next == "R":
			result = "R"
			return result
		
		# otherwise if next is another workflow, run through it
		elif ":" not in next:
			result = Sort(part, next)
			return result
		
		# if found result, stop searching
		if result != "":
			break
		
		step += 1

def Compare (op, rating, check, true, false):
	# compare the value against check then return result
	if op == "<":
		if rating < check:
			return true
		else:
			return false
	
	elif op == ">":
		if rating > check:
			return true
		else:
			return false

#################################
input = IN[0]

rules = {}		# dict of workflow in input
parts = []		# list of all parts in input

accepted = ["ACCEPTED:"]	# list of accepted parts
rejected = ["REJECTED:"]	# list of rejected parts
ratingParts = []	# summed ratings for accepted parts
ratingSum = 0		# SOLUTION | sum of accepted part ratings
#################################

# split up input into rules and parts
for line in input:
	if line[0] != "{":
		rules[line.split("{")[0]] = line.split("{")[1][:-1]
	else:
		parts.append(line[1:-1])

# run through each part to determine if accept or reject
for part in parts:
	outcome = Sort(part)
	if outcome == "A":
		accepted.append(part)
	elif outcome == "R":
		rejected.append(part)

# sum up the x,m,a,s values of the accepted parts
for part in accepted[1:]:
	partRating = 0
	for rating in part.split(","):
		r = int(rating[2:])
		partRating += r
	ratingParts.append(partRating)
	ratingSum += partRating

# visualize the rules
vis = []
for rule in rules:
	vis.append("[%s]: %s" %(rule, rules[rule]))

OUT = [ratingSum, ratingParts], [vis, parts], accepted, rejected
