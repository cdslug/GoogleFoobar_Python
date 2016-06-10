import timeit

def answer(document, searchTerms):
	documentSplit = document.split(" ")
	# encoder = generateEncoder(documentSplit, searchTerms)
	# encodedDocument = encodeStrings(documentSplit, encoder)
	
	# print "Encoded Document: " + str(document) + " = " + str(encodedDocument) + ", terms = " + str(range(len(searchTerms)))
	# print "Encoder: " + str(encoder)
	# encodedTerms = range(len(searchTerms))
	# encodedSnippet = searchForSnippets(encodedDocument,encodedTerms,len(searchTerms))
	# print "Encoded Snippet: " + str(encodedSnippet)
	# decoder = generateDecoder(encoder)
	# decodedSnippet = decodeNumbers(encodedSnippet,decoder)
	# return " ".join(decodedSnippet)
	return " ".join(searchForSnippets(documentSplit, searchTerms,len(searchTerms)))

def generateEncoder(stringList, searchTerms):
	encoding = {}
	index = 0
	offset = len(searchTerms)
	for s in stringList:
		if s in searchTerms:
			encoding[s] = searchTerms.index(s)
		else:
			encoding[s] = offset + index
			index += 1
	return encoding

def encodeStrings(documentSplit, encoding):
	encodedDocument = []
	for dS in documentSplit:
		encodedDocument.append(encoding[dS])
	return encodedDocument

def generateDecoder(encoder):
	decoder = {}
	for key,value in encoder.iteritems():
		decoder[value] = key
	return decoder

def decodeNumbers(encodedList, decoder):
	decodedSnippetList = []
	for eL in encodedList:
		decodedSnippetList.append(decoder[eL])
	return decodedSnippetList

def memoize(func):
	memo = {}
	def helper(input1,input2,input3):
		input1T = tuple(input1)
		input2T = tuple(input2)
		if (input1T,input2T,input3) not in memo:
			memo[(input1T,input2T,input3)] = func(input1,input2,input3)
		return memo[(input1T,input2T,input3)]
	return helper

def checkForAllTerms(subDocument, searchTerms,d):
	for sT in searchTerms:
		if sT not in subDocument:
			return False
	return True

def searchForSnippets(documentSplit,searchTerms,searchWidth):
	snippetA = snippetB = shortestSnippet = []
	if len(documentSplit) < searchWidth:
		return []
	elif checkForAllTerms(documentSplit[:searchWidth],searchTerms,3) == True:
		return documentSplit[:searchWidth]
	else:
		snippetA = searchForSnippets(documentSplit, searchTerms, searchWidth + 1)
		snippetB = searchForSnippets(documentSplit[1:],searchTerms,searchWidth)


	if snippetA != []:
		if snippetB != []:
			if len(snippetA) == len(snippetB):
				shortestSnippet = snippetA #finds words starting earliest
			elif len(snippetA) < len(snippetB):
				shortestSnippet = snippetA
			else:
				shortestSnippet = snippetB
		else:
			shortestSnippet = snippetA
	else:
		shortestSnippet = snippetB

	return shortestSnippet

checkForAllTerms = memoize(checkForAllTerms)
searchForSnippets = memoize(searchForSnippets)

inputs = []
inputs.append(["what is this who are you where am i how do you do where octo flat mat share do water haven dorag",["who", "where", "how"],"who are you where am i how"])
inputs.append(["many google employees can program",["google", "program"],"google employees can program"])
inputs.append(["world there hello hello where world",["hello","world"],"world there hello"])
inputs.append(["a b c d a",["a","c","d"],"c d a"])
inputs.append(["a b a b a b",["a","b"],"a b"])
inputs.append(["a b",["a","b"],"a b"])
print timeit.timeit(lambda:answer(inputs[0][0], inputs[0][1]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0],i[1])
	print "Answer = " + str(ans) + ", real = " + str(i[2])
	assert(ans == i[2])
	print "Passed Test Case #" + str(index) + "\n"