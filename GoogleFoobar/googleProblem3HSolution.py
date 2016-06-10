import timeit

def answer(minionStats):
	minionStatsIndexed = []
	for index,mS in enumerate(minionStats):
		print "minionStat = " + str(mS[0])
		minionStatsIndexed.append((mS,index,timeScore(mS)))
	minionStatsIndexed.sort(key = lambda mS: (mS[2],mS[0][0],mS[0][1],mS[0][2]))
	minionIndeces = [mSI[1] for mSI in minionStatsIndexed]
	return minionIndeces

def timeScore(minionStat):
	return minionStat[0] * minionStat[2] / minionStat[1]


inputs = []
inputs.append([[[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]],[2,3,0,1]])
inputs.append([[[5, 1, 5], [10, 1, 2]],[1,0]])
inputs.append([[[8, 2, 3],[2, 1023, 1024], [1, 1, 12], [6, 2, 4], [6, 1, 2]],[1,2,4,3,0]])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index) + "\n"
	else:
		print "Failed Test Case #" + str(index) + "\n"