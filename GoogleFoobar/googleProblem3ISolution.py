import timeit

def answer(x):
	# counter = 0
	###thought these would be faster when removing in the while searches, wrong
	# # x = [min(i,i[::-1]) for i in x]
	# # x.sort()
	# while x != []:
	# 	x0 = x[0]
	# 	x0r = x0[::-1]
	# 	x = x[1:]
	# 	### filtering is actually slower
	# 	# x = filter(lambda a: a != x0, x)
	# 	# x = filter(lambda a: a != x0r, x)
	# 	while x0 in x:
	# 		x.remove(x0)
	# 	while x0r in x:
	# 		x.remove(x0r)
	# 	counter += 1

	xSet = set([min(i,i[::-1]) for i in x])
	return len(xSet)


inputs = []
inputs.append([["bar", "woof","bar","woof","rab","foow","bar","","rab","woof","a","aa","aaa","ab","aab"],8])
inputs.append([["foo", "bar", "oof", "bar"],2])
inputs.append([["x", "y", "xy", "yy", "", "yx"],5])


print timeit.timeit(lambda:answer(inputs[0][0]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0])
	print "Answer = " + str(ans) + ", real = " + str(i[1])
	# assert(ans == i[1])
	if ans == i[1]:
		print "Passed Test Case #" + str(index) + "\n"
	else:
		print "Failed Test Case #" + str(index) + "\n"