intervals = []
intervals.append([[[1, 3], [3, 6]], 5])
intervals.append([[[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]], 16])

def answer(intervals):
	intervals.sort(key = lambda li: li[0])
	print intervals

	totalTime = 0
	startPos = endPos = 0
	for i in intervals:
		if i[1] > endPos:
			if i[0] > endPos:
				startPos = i[0]
			else:
				startPos = endPos
				print "ELSE: startPos = " + str(startPos)
			endPos = i[1]
			totalTime += endPos - startPos

			print "totalTime = " + str(totalTime)
	return totalTime

for index, i in enumerate(intervals):
	assert(answer(i[0]) == i[1])
	print "Passed Test Case #" + str(index)