import timeit
import math

def answer(x):
	x = x-1
	weightDictionary = {1:"L",2:"-",0:"R"}
	weights = []
	i = 0
	while x >= 0:
		weights.append(int(x/math.pow(3,i))%3)
		x = x - math.pow(3,i)
		i += 1
	weightPosition = [weightDictionary[w] for w in weights]
	return weightPosition



inputs = []
inputs.append([1,["R"]])
inputs.append([2,["L","R"]])
inputs.append([3,["-","R"]])
inputs.append([4,["R","R"]])
inputs.append([5,["L","L","R"]])
inputs.append([6,["-","L","R"]])
inputs.append([7,["R","L","R"]])
inputs.append([8,["L","-","R"]])
inputs.append([9,["-","-","R"]])
inputs.append([10,["R","-","R"]])
inputs.append([11,["L","R","R"]])
inputs.append([12,["-","R","R"]])
inputs.append([13,["R","R","R"]])
inputs.append([14,["L","L","L","R"]])


print timeit.timeit(lambda:answer(1000000000), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index + 1) + "\n"
	else:
		print "Failed Test Case #" + str(index + 1) + "\n"