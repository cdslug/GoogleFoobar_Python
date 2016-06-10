import timeit

def answer(words):
	pairedLetters = splitByHeirarchy(words)
	letterDict = pairsToDict(pairedLetters)
	return determineOrder(letterDict)

def splitByHeirarchy(words):
### Input:
###		list of words sorted alphabetically according to the desired language
### Output:
###		For all words, pair up each letter with the letter from the next word that follows
### Example:
###			['z','y','xy'] => [('z','y'),('y','x')]
	letterPairs = []

	### Base case if there are no words to compare
	### My implementation should not reach this
	### It would be a bit faster without, but I'll keep it for safety
	if len(words) <= 1:
		letterPairs = []
	else:
		#order1 is a list of sorted letters, first letters from each word
		order1 = []
		for w in words:
			if w[0] not in order1:
				order1.append(w[0])
		letterPairs += splitToPairs(order1)

		# print "Letter Pairs: " + str(letterPairs)
		### Remove first letter of all words and group them by first letter
		### This is to preserve alphabetization 
		subStrings = {}
		for w in words:
			if w[1:] != "":
				if w[0] in subStrings:
					subStrings[w[0]].append(w[1:])
				else:
					subStrings[w[0]] = [w[1:]]
		words2 = []
		for ss in subStrings.values():
			#a single substring is useless without another for comparison
			if len(ss) > 1:
				letterPairs += splitByHeirarchy(ss)

		# print "letterPairs: " + str(letterPairs)

	return letterPairs

def splitToPairs(order):
### Input:
###		list of letters in their relative alphabetic order
### Output:
###		Pair up each letter with the letter that follows it
###		The last letter does not get it's own tuple
### Example:
###			['a','b','c'] => [('a','b'),('b','c')]
	orderTuples = []
	for index in range(len(order)-1):
		orderTuples.append((order[index],order[index+1]))
	return orderTuples

def pairsToDict(pairs):
### Input:
###		list of tuples signifying relative alphabetic order
### Output:
###		dictionary with letters as keys and a list of following letters as values
### Example:
###		[('a','b'),('a','c'),('b','c')] => {'a':['b','c'],'b':['c']}
	letterDict = {}
	for p in pairs:
		if p[0] in letterDict:
			letterDict[p[0]].append(p[1])
		else:
			letterDict[p[0]] = [p[1]]
	return letterDict


def determineOrder(letterDict):
### Input:
###		dictionary with letters as keys and a list of following letters as values
### Output:
###		string with letters sorted alphabetically for a desired language
### Example:
###		{'a':['b','c'],'b':['c']} => "abc"
### Explanation:
###		No other letters will have the first letter of the alphabet after it.
###		Find the first letter by subtracting following-letters from leading-letters
###		Remove the first letter from the dictionary and repeat
###		The last dicitonary entry should only have 1 letter as its value
###		This single letter value is the last letter in the alphabet

	finalOrder = ""
	# for the last letter
	# 	always checking 0 should be better than checking len(letterDict) == 1
	for i in range(len(letterDict))[::-1]:
		primaryLetters = set(letterDict.keys())
		secondaryLetters = set(reduce(lambda x,y: x + y,letterDict.values()))
		currentLetter = list(primaryLetters - secondaryLetters)[0]
		finalOrder += currentLetter

		# last letter
		if i == 0:
			finalOrder += letterDict.values()[0][0]

		letterDict.pop(currentLetter,None)
	print "Final Order: " + str(finalOrder)
	return finalOrder
	

words = []
words.append([["aaaa","aaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaz","aaab","aaac","aabz","aabzz","aaza","bc","bd","bf","by","bz"],"abcdfyz"])
words.append([["y", "z", "xy"],"yzx"])
words.append([["ba", "ab", "cb"],"bac"])
words.append([["aac","aar","bat","car","cat","cbc","cbt"],"abcrt"])


for index, i in enumerate(words):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	assert(ans == i[1])
	print "Passed Test Case #" + str(index) + "\n"

with open("/usr/share/dict/words","r") as fin:
	wordDict = fin.readlines()
	wordDict = [w.lower() for w in wordDict]
	print timeit.timeit(lambda:answer(wordDict), number=1)

