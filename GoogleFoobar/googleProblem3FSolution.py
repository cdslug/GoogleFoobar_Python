import timeit

def answer(document, searchTerms):
	documentSplit = document.split(" ")
	# encoder = generateEncoder(documentSplit, searchTerms)
	# encodedDocument = encodeStrings(documentSplit, encoder)
	
	# print "Encoded Document: " + str(document) + " = " + str(encodedDocument) + ", terms = " + str(range(len(searchTerms)))
	# print "Encoder: " + str(encoder)
	# encodedTerms = range(len(searchTerms))
	# encodedSnippet = searchForSnippets(encodedDocument,encodedTerms,False)
	# print "Encoded Snippet: " + str(encodedSnippet)
	# decoder = generateDecoder(encoder)
	# decodedSnippet = decodeNumbers(encodedSnippet,decoder)
	# return " ".join(decodedSnippet)
	return " ".join(searchForSnippets(documentSplit, searchTerms,False))

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

def searchForSnippets(documentSplit,searchTerms, started):

	#document guaranteed to contain all searchTerms
	#this means documentSplit will never be empty if searchTerms is occupied
	shortestSnippet = []
	if searchTerms == [] or documentSplit == []:
		# print "Found []!!!!XXXX"
		return []
	else:
		#side B tries to match the first word
		snippetB = []
		if documentSplit[0] in searchTerms:
			# print "B: DocumentSplit = " + str(documentSplit) + "\tsearchTerms = " + str(searchTerms)
			# print "Found! " + str(documentSplit[0:1]) + " in searchTerms " + str(searchTerms) + ", " + str(documentSplit)
			index = searchTerms.index(documentSplit[0])
			searchTermsB = searchTerms[0:index] + searchTerms[index+1:]
			# print "now searchTermsB is " + str(searchTermsB)
			if searchTermsB == []:
				snippetB = documentSplit[0:1]
				# print "FOUND THE END: " + str(snippetB)
			elif len(documentSplit) > 0:
				snippetB = searchForSnippets(documentSplit[1:],searchTermsB, True)
				# print "Appending: " + str(documentSplit[0:1]) + " + " + str(snippetB)
				if snippetB != []:
					snippetB = documentSplit[0:1] + snippetB
			#shortcut
			if len(snippetB) == len(searchTerms):
				# print "SHORTCUT!\t" + str(documentSplit[0:1])
				return snippetB
			# else:
			# 	print "NOPE!CUT!"
		#side A skips the first word and looks further
		snippetA = []
		if len(documentSplit) > 0:
			# print "A: DocumentSplit = " + str(documentSplit) + "\tsearchTerms = " + str(searchTerms)
			snippetA = searchForSnippets(documentSplit[1:],searchTerms,started)
			if snippetA != [] and started:
				snippetA = documentSplit[0:1] + snippetA
		# else:
			# print "NoFind " + str(documentSplit[0:1]) + " in searchTerms " + str(searchTerms) + ", " + str(documentSplit)
		if snippetA != []:
			if snippetB != []:
				if len(snippetA) == len(snippetB):
					shortestSnippet = snippetB #finds words starting earliest
				elif len(snippetA) < len(snippetB):
					shortestSnippet = snippetA
				else:
					shortestSnippet = snippetB
			else:
				shortestSnippet = snippetA
		else:
			shortestSnippet = snippetB
	# print "docSplit = " + str(documentSplit) + ", searchTerms = " + str(searchTerms) + ", shtS = " + str(shortestSnippet) + ", sA = " + str(snippetA) + ", sB = " + str(snippetB)
	return shortestSnippet

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