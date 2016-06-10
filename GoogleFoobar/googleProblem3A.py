import operator

def answer(digest):
	print digest
	message = [0]
	for d in digest:
		for i in range(256):
			if d == operator.xor(129*i,message[-1]) % 256:
				message.append(i)
				break
	print message[1:]
	return message[1:]

def hashFunc(message):
	digest = []
	for index in range(len(message)):
		temp = 129*message[index]
		if index > 0:
			temp = operator.xor(temp,message[index-1])
		#otherwise do nothing, message[-1] is 0
		temp %= 256
		digest.append(temp)
	return digest

digest = []
digest.append([[0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]])
digest.append([[0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]])

test1 = [1,28,17,72,89,27,9,0,0,3,0,255,1,1,1,1]
digest.append([hashFunc(test1),test1])

for index, i in enumerate(digest):
	assert(answer(i[0]) == i[1])
	print "Passed Test Case #" + str(index)