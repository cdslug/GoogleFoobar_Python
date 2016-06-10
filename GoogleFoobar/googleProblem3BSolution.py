#http://codereview.stackexchange.com/questions/91317/google-foobar-challenge-save-beta-rabbit-in-python

import timeit

def memoize(func):
	memo = {}
	def helper(food, grid):
		list2Tuple = tuple([tuple(g) for g in grid])
		if (food, list2Tuple) not in memo:
			memo[(food, list2Tuple)] = func(food,grid)
		return memo[(food, list2Tuple)]
	return helper

def answer(food, grid):
	if food < 0:
		return -1
	if len(grid) == 1 and len(grid[0]) == 1:
		if grid[0][0] <= food:
			return food - grid[0][0]
		else:
			return -1

	rightMove = downMove = -1
	if len(grid[0]) > 1:
		rightMove = answer(food - grid[0][0], [g[1:] for g in grid])
	if len(grid) > 1:
		downMove = answer(food - grid[0][0], grid[1:])
	
	#make it so -1 is only returned if it is inevitable 
	if rightMove == -1:
		rightMove = downMove
	if downMove == -1:
		downMove = rightMove

	return min([rightMove,downMove])


	
inputs = []
large = [range(11) for i in range(11)]
# inputs.append([200,large,0])
inputs.append([7,[[0, 2, 5], [1, 1, 3], [2, 1, 1]],0])
inputs.append([12,[[0, 2, 5], [1, 1, 3], [2, 1, 1]],1])
inputs.append([20,[[0, 2, 5], [5, 1, 3], [5, 5, 5]],0])
inputs.append([13,[[0, 2, 5], [5, 1, 3], [5, 5, 5]],0])
inputs.append([0,[[0, 2, 5], [5, 1, 3], [5, 5, 5]],-1])
inputs.append([0,[[0]],0])

# answer = memoize(answer)

print timeit.timeit(lambda:answer(inputs[0][0], inputs[0][1]), number=1)
for index, i in enumerate(inputs):
	ans = answer(i[0], i[1])
	print "Answer = " + str(ans) + ", real = " + str(i[2])
	assert(ans == i[2])
	print "Passed Test Case #" + str(index)