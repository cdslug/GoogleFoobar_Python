import timeit
import math

def answer(population, x, y, strength):
	stack = [(x,y)] #contains tuples of (x,y) coordinates
	checked = {} #look up (x,y) coordinates to see if infection attempted
	while len(stack) > 0:
		x,y = stack[0]
		stack = stack[1:]
		checked[(x,y)] = -1
		if population[y][x] <= strength:
			population[y][x] = -1

			if x > 0  and (x-1,y) not in checked:
				stack.append((x-1,y))
			if y > 0 and (x,y-1) not in checked:
				stack.append((x,y-1))
			if x + 1 < len(population[0]) and (x+1,y) not in checked:
				stack.append((x+1,y))
			if y + 1 < len(population) and (x,y+1) not in checked:
				stack.append((x,y+1))
	return population

inputs = []
inputs.append([[[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]],2,1,5,[[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]])
inputs.append([[[1, 2, 3], [2, 3, 4], [3, 2, 1]],0,0,2,[[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]])


print timeit.timeit(lambda:answer(inputs[0][0],inputs[0][1],inputs[0][2],inputs[0][3]), number=10)

for index, i in enumerate(inputs):
	ans = answer(i[0],i[1],i[2],i[3])
	print "Answer = " + str(ans) + ", real = " + str(i[4])
	# assert(ans == i[1])
	if ans == i[4]:
		print "Passed Test Case #" + str(index + 1) + "\n"
	else:
		print "Failed Test Case #" + str(index + 1) + "\n"