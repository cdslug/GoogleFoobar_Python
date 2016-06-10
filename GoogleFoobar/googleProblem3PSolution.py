import timeit
import math

def answer(x):
    if x == 0:
        return 0
    else:
        sol = x % 9
        return sol if sol != 0 else 9

def answerConfirm(n):
	if n < 10:
		return n
	else:
		return answerConfirm(sum([int(d) for d in str(n)]))

inputs = []
inputs.append([1235,2])
inputs.append([12345,6])



print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"

for n in range (2<<10):
	if answer(n) != answerConfirm(n):
		print "%9 shortcut failed with " + str(n)
print "PASSED EXHAUSTIVE TEST"