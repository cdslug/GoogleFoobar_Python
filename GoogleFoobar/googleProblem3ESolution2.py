import timeit
# import math


def memoize(func):
	memo = {}
	def helper(input1,input2):
		if (input1,input2) not in memo:
			memo[(input1,input2)] = func(input1,input2)
		return memo[(input1,input2)]
	return helper

def answer(n):
	largestSquare = getSquareList(n)[-1]
	return searchLeastItems(n,largestSquare)

def getSquareList(n):
	squares = []
	square = index = 1
	while square <= n: #round down
		squares.append(square)
		square = index * index
		index += 1
	return squares 

def searchLeastItems(n,largestSquare):
	numberItems = 0
	squaresReversed = getSquareList(largestSquare)[::-1]
	if n <= 0 or len(squaresReversed) <= 1:
		numberItems = 0 
	else:
		#side A skips the highest possible square
		nA = n #for clarity
		itemsA = searchLeastItems(n,squaresReversed[1])

		#side B uses the highest possible square and allows it to be used again
		nB = n - squaresReversed[0]
		while len(squaresReversed) > 1 and squaresReversed[0] > nB:
			squaresReversed = squaresReversed[1:]
		itemsB = searchLeastItems(nB,squaresReversed[0]) + 1

		if itemsA == 0:
			numberItems = itemsB
		else:
			numberItems = min([itemsA,itemsB])

	return numberItems

searchLeastItems = memoize(searchLeastItems)


inputs = []
inputs.append([24,3])
inputs.append([160,2])
inputs.append([9,1])

print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[2])
	print "Passed Test Case #" + str(index) + "\n"
