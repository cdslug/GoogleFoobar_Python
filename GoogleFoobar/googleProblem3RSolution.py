import timeit
import math

def answer(x):
	if x == 0:
		return 1
	else:
		return pow(7,x) + answer(x-1)

# def answer(x):
# 	result = 0
# 	while x >= 0:
# 		result += pow(7,x)
# 		x -= 1
# 	return result

inputs = []
inputs.append([1,8])
inputs.append([2,57])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"