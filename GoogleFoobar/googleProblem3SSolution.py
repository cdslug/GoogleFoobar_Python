import timeit
import math

def answer(numbers):
	counter = 0
	pirateRef = 0
	#dictionary of pirate ID numbers and number of order I talked to him
	pirateDict = {}
	while True:
		if pirateRef not in pirateDict:
			pirateDict[pirateRef] = counter
			pirateRef = numbers[pirateRef]
			counter += 1
		else:
			return counter - pirateDict[pirateRef]

inputs = []
inputs.append([[1,3,0,1],2])
inputs.append([[1,0],2])
inputs.append([[1,2,1],2])
inputs.append([[1,4,0,8,7,0,3,3,10,0,6],4])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"