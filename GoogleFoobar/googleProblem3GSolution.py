import timeit

def answer(heights):
	waterArea = 0
	while len(heights) > 2:
		heightsAndIndeces = []
		for index,h in enumerate(heights):
			heightsAndIndeces.append((h,index))
		heightsAndIndecesSorted = heightsAndIndeces
		heightsAndIndecesSorted.sort(key = lambda hI: hI[0])
		heightsAndIndecesSorted = heightsAndIndecesSorted[::-1]

		#reminder:(height,index)

		hutchA = hutchB = hutchC = []
		hutchesTop3 = heightsAndIndecesSorted[0:3]
		hutchesTop3.sort(key = lambda h:h[1])
		hutchA = hutchesTop3[1]
		hutchB = hutchesTop3[0]
		hutchC = hutchesTop3[2]

		print "hutchA Index: " + str(hutchA[1]) + ", hutchB Index: " + str(hutchB[1]) + ", hutchC Index: " + str(hutchC[1])

		#first check corner case if middle is less than two other tallest hutches
		if hutchA[0] < hutchB[0] and hutchA[0] < hutchC[0]:
			#checking indices
			if hutchB[1] < hutchC[1]:
				waterArea += measureWater(heights[hutchB[1]:hutchC[1] + 1])
			else:
				waterArea += measureWater(heights[hutchC[1]:hutchB[1] + 1])
		else:
			#checking indices
			if hutchA[1] < hutchB[1]:
				waterArea += measureWater(heights[hutchA[1]:hutchB[1] + 1])
			else:
				waterArea += measureWater(heights[hutchB[1]:hutchA[1] + 1])

			if hutchA[1] < hutchC[1]:
				waterArea += measureWater(heights[hutchA[1]:hutchC[1] + 1])
			else:
				waterArea += measureWater(heights[hutchC[1]:hutchA[1] + 1])
		
		hutchMin = min(hutchA[1],hutchB[1],hutchC[1])
		hutchMax = max(hutchA[1],hutchB[1],hutchC[1])
		heights = heights[:hutchMin + 1] + heights[hutchMax:]
		
	return waterArea

def measureWater(heightsSubsection):
	print "Measuring: " + str(heightsSubsection)
	waterArea = 0
	lowerWall = min(heightsSubsection[0],heightsSubsection[-1])
	for index in range(1,len(heightsSubsection) - 1):
		waterArea += (lowerWall - heightsSubsection[index])
	return waterArea

inputs = []
inputs.append([[1, 4, 2, 5, 1, 2, 3],5])
inputs.append([[1, 2, 3, 2, 1],0])
inputs.append([[3,1,1,3,1,3],6])
inputs.append([[2,1,2],1])
inputs.append([[3,2,2,4,2,2,5],6])
inputs.append([[4,2,2,3,2,2,5],9])
inputs.append([[2,1,3,2,3],2])

print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index) + "\n"
	else:
		print "Failed Test Case #" + str(index) + "\n"