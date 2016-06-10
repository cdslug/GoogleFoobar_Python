import timeit
import math

def answer(s):
	rpnPrepAdd = s.split('+')
	rpnPrepMult = [r.split('*') for r in rpnPrepAdd]
	rpnWorkMult = [''.join(r) + '*'*(len(r) - 1) for r in rpnPrepMult]
	rpnWorkAdd = ''.join(rpnWorkMult) + '+'*(len(rpnWorkMult)-1)
	return rpnWorkAdd

inputs = []
inputs.append(["2+3*2","232*+"])
inputs.append(["2*4*3+9*3+5","243**93*5++"])
inputs.append(['2*3+6*7+4*5','23*67*45*++'])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"