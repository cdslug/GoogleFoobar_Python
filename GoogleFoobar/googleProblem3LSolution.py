import timeit
import math

def answer(x):
	if sum(x)%len(x) != 0:
		return len(x) - 1
	else:
		return len(x)

inputs = []
inputs.append([[1,11,2,10,3,9,4,8,5,7],10])
inputs.append([[1,11,2,10,3,9,4,8,5,6],9])
inputs.append([[1,11,2,10,3,9,4,8,6,7],9])
inputs.append([[1,4,1],3])
inputs.append([[1,2],1])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index + 1) + "\n"
	else:
		print "Failed Test Case #" + str(index + 1) + "\n"