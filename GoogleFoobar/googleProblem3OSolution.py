import timeit
import math

def answer(n):
	for b in range(2,1001):
		if checkPalindrome(getBaseBRepresentation(n,b)) == True:
			return b
	return -1 #should not happen

def getBaseBRepresentation(number,b):
	baseBRep = []
	while number != 0:
		baseBRep.append(number%b)
		number = number/b
	if baseBRep == []:
		baseBRep.append(0)
	return baseBRep

def checkPalindrome(inputN):
	for index in range(int((len(inputN)+1)/2)):
		if inputN[index] != inputN[-1 * (index + 1)]:
			return False
	return True

inputs = []
inputs.append([0,2])
inputs.append([42,4])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"