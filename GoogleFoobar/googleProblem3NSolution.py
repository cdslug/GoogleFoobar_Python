import timeit
import math

def answer(x,y,z):
	possibilities = [(x,y,z),(x,z,y),(y,x,z),(y,z,x),(z,x,y),(z,y,x)]
	correctDates = set([""])
	for index in range(len(possibilities)):
		correctDates.add(checkDateValid(possibilities[index]))

	# print "correctDates: " + str(correctDates)
	correctDates = correctDates.difference({""})
	if len(correctDates) != 1:
		return "Ambiguous"
	else:
		dateString = list(correctDates)
		return dateString[0]



def checkDateValid(dateInput):
	month,day,year = dateInput
	if 0 < month and month <= 12 and 0 < day:
		#months with 31 days
		if ((month - 1) % 7)%2 == 0 and day <= 31:
			return "%02d" % month + "/" + "%02d" % day + "/" + "%02d" % year
		elif month == 2 and day <= 28:
			return "%02d" % month + "/" + "%02d" % day + "/" + "%02d" % year
		elif ((month - 1) % 7)%2 == 1 and month != 2 and day <= 30:
			return "%02d" % month + "/" + "%02d" % day + "/" + "%02d" % year
	return ""

inputs = []
inputs.append([1,1,91,"01/01/91"])
inputs.append([19,19,3,"03/19/19"])
inputs.append([2,30,3,"Ambiguous"]) #
inputs.append([1,2,3,"Ambiguous"]) #month day and year can swap
inputs.append([7,17,91,"07/17/91"])
inputs.append([12,12,91,"12/12/91"]) #month and day are the same
inputs.append([12,11,15,"Ambiguous"]) #
inputs.append([2,29,15,"02/15/29"])
inputs.append([4,31,30,"04/30/31"])
inputs.append([4,31,90,"Ambiguous"])
inputs.append([8,31,91,"08/31/91"])
inputs.append([8,32,31,"08/31/32"])
inputs.append([2,29,50,"Ambiguous"])

inputs.append([1,31,32,"01/31/32"])
inputs.append([1,30,31,"Ambiguous"])
inputs.append([3,31,32,"03/31/32"])
inputs.append([3,30,31,"Ambiguous"])
inputs.append([5,31,32,"05/31/32"])
inputs.append([5,30,31,"Ambiguous"])
inputs.append([7,31,32,"07/31/32"])
inputs.append([7,30,31,"Ambiguous"])
inputs.append([8,31,32,"08/31/32"])
inputs.append([8,30,31,"Ambiguous"])
inputs.append([10,31,32,"10/31/32"])
inputs.append([10,30,31,"Ambiguous"])
inputs.append([12,31,32,"12/31/32"])
inputs.append([12,30,31,"Ambiguous"])
inputs.append([4,30,31,"04/30/31"])
inputs.append([4,29,30,"Ambiguous"])
inputs.append([6,30,31,"06/30/31"])
inputs.append([6,29,30,"Ambiguous"])
inputs.append([9,30,31,"09/30/31"])
inputs.append([9,29,30,"Ambiguous"])
inputs.append([11,30,31,"11/30/31"])
inputs.append([11,29,30,"Ambiguous"])
inputs.append([2,28,29,"02/28/29"])
inputs.append([4,29,30,"Ambiguous"])

inputs.append([2,28,28,"02/28/28"])
inputs.append([2,2,28,"Ambiguous"])
inputs.append([13,6,31,"06/13/31"])
inputs.append([3,3,3,"03/03/03"])


print timeit.timeit(lambda:answer(inputs[0][0],inputs[0][1],inputs[0][2]), number=1)

for index, i in enumerate(inputs):
	ans = answer(i[0],i[1],i[2])
	print "Answer = " + str(ans) + ", real = " + str(i[3])
	# assert(ans == i[1])
	if ans == i[3]:
		print "passed Test Case #" + str(index + 1) + "\n"
	else:
		print "FAILED Test Case #" + str(index + 1) + "\n"