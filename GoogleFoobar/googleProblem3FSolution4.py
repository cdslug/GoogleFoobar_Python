import timeit

def answer(document, searchTerms):
	documentSplit = document.split(" ")

	return " ".join(searchForSnippets(documentSplit, searchTerms))

def checkForAllTerms(subDocument, searchTerms):
	for sT in searchTerms:
		if sT not in subDocument:
			return False
	return True

def searchForSnippets(documentSplit,searchTerms):
	snippetA = snippetB = shortestSnippet = []
	lenDoc = len(documentSplit)
	for index1 in range(len(searchTerms),lenDoc + 1):
		for index2 in range(lenDoc):
			if index1 + index2 > lenDoc:
				break
			elif checkForAllTerms(documentSplit[index2:index2 + index1],searchTerms) == True:
				return documentSplit[index2:index2 + index1]


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
	# assert(ans == i[2])
	print "Passed Test Case #" + str(index) + "\n"