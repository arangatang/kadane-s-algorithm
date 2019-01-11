import sys


def KadanesAlgo(A, maxLength):
	# Runs through the array once utilizing dynamic programming for fast runtime
	# Timecomplexity: O(n)
	# Calculates the largest sum of a continous subset of a maximum length
	# Based on Kadanes algorithm, further explained here
	# https://en.wikipedia.org/wiki/Maximum_subarray_problem

	# :param A int[] the input array of ints to search through
	# :param maxLength int describes the maximum allowed length of a sequence
	# :return the maximum sum of a continous sequence array A
	# :rtype int
	
	# a sequence of zero length has no value
	if(maxLength == 0):
		return 0

	maxSoFar = maxEndingHere = A[0]
	length = index = 1
	segmentStart = 0
	for number in A[1:]:
		#This handles the cutoff for the maximum allowed length of a sequence
		if(length == maxLength):
			maxEndingHere -= A[segmentStart]
			segmentStart += 1
		else: 
			length += 1
		
		#This calculates wether or not the next number is larger than the current
		#sequence of values + the next number
		#if so it starts a new sequence based on the next number
		if(number > (maxEndingHere + number)):
			length = 1
			segmentStart = index
			maxEndingHere = number
		else:
			maxEndingHere += number

		# This checks wether the current sequence of numbers has a larger sum than
		# the largest sum currently found
		if(maxSoFar < maxEndingHere):
			maxSoFar = maxEndingHere
		index += 1
	return maxSoFar


def convertToDifferences(A):
	# Converts values of an input array with ints to their pairwise differences
	# Timecomplexity: O(n)
	# e.g.  [1, 2, -3] => [1, 5]
	# :param A [] input array to be modified
	# :return the array of distances
	# :rtype int[]
	differencesArray = []
	prevNumber = A[0]
	for number in A[1:]:
		differencesArray.append(abs(number - prevNumber))
		prevNumber = number
	return differencesArray


def main():
	# This is the main control function for the program
	# Ensures correctness of inputs

	if len(sys.argv) < 3: 
		print('too few arguments, usage: find_subsequences.py path_to_data_file max_subequence_length method')
		return 1
	
	try:
		inputFile = sys.argv[1]
		windowSize = int(sys.argv[2])
		methodToUse = sys.argv[3]
	except:
		print('parameters are malformed usage string int string')
		return 1

	try:
		file = open(inputFile, 'r')
		line = file.readline()
		file.close()
	except:
		print("unable to open the file, check the path")
		return 1

	try:
		numberArray = list(map(int, line.split()))
	except:
		print("the file does not contain ints")
		return 1

	if(methodToUse == "differences"):
		numberArray = convertToDifferences(numberArray)
		# We need to modify the window size since the conversion to distances causes
		# the array we work on to become one element smaller
		windowSize -= 1
	elif(methodToUse != "values"):
		print("The desired method is undefined, usage: differences | values")
		return 1

	print(KadanesAlgo(numberArray, windowSize))
	return 0


if __name__ == '__main__':
    exit(main())