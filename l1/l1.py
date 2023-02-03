# CSCI 331 - Lab 1
# Author: Jasper Charlinski (658366497)
# Due: Jan 25th, 2023

# This program finds the path with maximum sum for a set
# of values. For example, by starting at the top of the triangle below and moving to
# adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# 3 + 7 + 4 + 9 = 23


from pytictoc import TicToc
import sys

class LabOne:

	al = [] # all lines
	result = 0

	def readFile(self, fn: str) -> None:

		try: # try to open provided input file, if successful: 

			file = open(fn, 'r')

			for line in file.readlines(): # for each line the in the provided file
				self.al.append(line.split()) # append each row of numbers as a list of characters 
				
			file.close()

		except: # if file was unable to open

			print('Error: ', fn, ' was unable to open')
			self.al.append([0]) 
			return


		if len(self.al) == 0: # if provided input file was empty

			print('Error: ', fn, ' is empty')
			self.al.append([0])
			return


		for i, line in enumerate(self.al): # for each index in the all lines (al) list, enumerate to keep track of index
			self.al[i] = [int(char) for char in line] # convert each character in line i to an integer 

		# for i in self.al: # print out all lists
		# 	print(i)

			

	def process(self) -> None:

		if len(self.al) == 1: # if there is only one integer in the list, nothing to calculate 

			return
		
		index = len(self.al) - 2 # variable to keep track of al index, starts at second to last index of al,
		# this is because it is the first list of nodes that have children.

		for line in self.al[ len(self.al) - 2 :: -1 ]: # for each list in al (minus the final index) starting from the back 
			
			for j in range(len(line)): # for each integer j in the list of the current index

				self.al[index][j] += max(self.al[index+1][j], self.al[index+1][j+1]) # j = j + the maximum of its children
	
			index -= 1 # decrement index



	def getResult(self) -> int:
		
		self.result = self.al[0][0] # result is the root / first integer in the first list of al

		return(self.result) 
		


if __name__ == '__main__':
	#DO NOT MODIFY THIS CODE
	t = TicToc()
	t.tic() # start timer

	solution = LabOne()
	solution.readFile(sys.argv[1])
	if solution.al:
		solution.process()

	print('*' * 7)
	print('*' * 13)
	print(solution.getResult())
	t.toc() #elapsed time
	print('*' * 13)

