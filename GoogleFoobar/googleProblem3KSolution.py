import timeit
import math

def answer(names):
	namesWithScore = [(n,nameScore(n)) for n in names]
	namesWithScore.sort(key = lambda nWS: (nWS[1],nWS[0]),reverse = True)
	print "namesWithScore = " + str(namesWithScore)
	return [n[0] for n in namesWithScore]

def nameScore(name):
	score = 0
	for n in name:
		score += ord(n) - ord("a") + 1
	return score

inputs = []
inputs.append([["waffle","ryan","jordi","aasqwerbzcv","doppleganger","beatrice","alcapone","auntjamima"],['aasqwerbzcv', 'doppleganger', 'auntjamima', 'alcapone', 'beatrice', 'ryan', 'jordi', 'waffle']])
inputs.append([["abcdefg", "vi"],["vi","abcdefg"]])
inputs.append([["al","cj"],["cj","al"]])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index + 1) + "\n"
	else:
		print "Failed Test Case #" + str(index + 1) + "\n"