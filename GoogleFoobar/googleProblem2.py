meetings = []
meetings.append([[[0, 1], [1,100], [1, 2], [2, 3], [3, 5], [4, 5]], 4]) #4
meetings.append([[[0, 1000000], [42, 43], [0, 1000000], [42, 43]], 1]) #1
meetings.append([[[0,1],[1,4],[2,3],[3,4],[4,5]], 4]) #4
meetings.append([[[1,12],[1,4],[2,5],[3,6],[4,7],[5,8],[6,9],[7,10],[8,11],[9,12],[12,13]], 4]) #4
meetings.append([[[1,2],[2,7],[3,5],[4,6],[7,8],[8,10],[9,11]], 4])
meetings.append([[[1,2],[2,7],[3,4],[4,8],[8,9],[9,12],[10,11]], 5])

def answer(meetings):
    # your code here
    meetings.sort(key=lambda li: li[0])
    print "\n" + str(meetings) + str("\n")
    return recursive2Answer(meetings)
    
def recursiveAnswer(meetings):
    if len(meetings) == 1:
        return 1

    leftSide = (meetings[1][0] >= meetings[0][1]) + recursiveAnswer(meetings[1:])
    rightSide = 0
    if len(meetings) >= 3:
    	rightSide = recursiveAnswer(meetings[2:])
    return max([leftSide,rightSide])


def answerSimple1(meetings):
    # your code here
    #passes 4/5 tests
    meetings.sort(key=lambda li: li[0])
    print meetings
    count = 1
    frontIndex = 0
    for endIndex in range(len(meetings)):
        if endIndex > frontIndex:
            if meetings[endIndex][0] >= meetings[frontIndex][1]:
                count += 1
                frontIndex = endIndex
    return count

#I submitted this solution. 50% of level 2 after submitting this
def answerSimple2(meetings):
	# your code here
    #passes 4/5 tests
    meetings.sort(key=lambda li: li[0])
    print meetings
    count = 1
    frontIndex = 0
    # lastEnding = meeting[0][1]
    for endIndex in range(len(meetings))[1:]:
        if meetings[endIndex][0] >= meetings[frontIndex][1]:
            count += 1
            frontIndex = endIndex
        else:
        	if meetings[endIndex][1] < meetings[frontIndex][1]:
        		frontIndex = endIndex
    return count

#this one works
def recursive2Answer(meetings):
	print meetings
	if len(meetings) == 1:
		return 1

	leftSide = rightSide = 0

	if meetings[1][0] >= meetings[0][1]:
		leftSide = 1 + recursive2Answer(meetings[1:])
	else:
		if len(meetings) >= 3:	
			leftSide = recursive2Answer([meetings[0]] + meetings[2:])
		else:
			leftSide = 1
		rightSide = recursive2Answer(meetings[1:])
	return max([leftSide,rightSide])

#doesn't work
def recursive3Answer(meetings):
	print meetings
	if len(meetings) == 1:
		return 1

	leftSide = rightSide = 0

	count = 1
	for index in range(len(meetings)):
		if index + 1 < len(meetings) and meetings[index + 1][0] >= meetings[index][1]:
			count + 1
		else:
			if len(meetings[index:]) >= 3:	
				leftSide = recursive3Answer([meetings[index]] + meetings[index + 2:])
			else:
				leftSide = 1
			rightSide = recursive3Answer(meetings[index + 1:])
			print "*** COUNT = " + str(count + recursive3Answer(meetings[index + 1:])) + " ***"
			return count + max([leftSide,rightSide])
	return count

for i,m in enumerate(meetings):
	assert(answerSimple2(m[0]) == m[1])
	print "Passed Test #" + str(i)