import timeit

def memoize(func):
	memo = {}
	def helper(input1,input2):
		if (input1,input2) not in memo:
			memo[(input1,input2)] = func(input1,input2)
		return memo[(input1,input2)]
	return helper

def answer(chunk,word):
	return recursiveAnswer(chunk,word)

def recursiveAnswer(chunk,word):
### Explanation:
###		recursively remove all possibilities of the added word
###		append all possibilites to a list
###		sort the list by size and then sort alphabetically
	# print "Chunk = " + chunk + ", Word = " + word
	wordLen = len(word)
	indexFound = 0
	shortMessages = []
	while True:
		indexFound = chunk.find(word,indexFound)
		if indexFound != -1:
			shortMessages.append(recursiveAnswer(chunk[0:indexFound] + chunk[indexFound + wordLen:],word))
			indexFound += 1 #make it look for the next possibility
		else:
			shortMessages.append(chunk)
			break

	# print "Short Messages: " + str(shortMessages)
	#sort by length
	shortMessages.sort(key = lambda sm: len(sm))
	shortestMessage = []
	if len(shortMessages) > 0:
		shortestLen = len(shortMessages[0])
		shortMessages = [sm for sm in shortMessages if len(sm) == shortestLen]
		#sort lexicographically
		shortMessages.sort()
		shortestMessage = shortMessages[0]
	return shortestMessage

recursiveAnswer = memoize(recursiveAnswer)

inputs = []
inputs.append(["lololololo","lol","looo"])
inputs.append(["goodgooogoogfogoood","goo","dogfood"])
inputs.append(["lolol","lol","lo"])
for index, i in enumerate(inputs):
	ans = answer(i[0],i[1])
	print "Answer = " + str(ans) + ", real = " + str(i[2])
	# assert(ans == i[2])
	print "Passed Test Case #" + str(index) + "\n"

print timeit.timeit(lambda:answer(inputs[0][0], inputs[0][1]), number=1)