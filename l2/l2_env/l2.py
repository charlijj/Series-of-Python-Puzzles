# CSCI 331 - Lab 2
# Author: Jasper Charlinski
# Due: Feb 8th, 2023

"""
This program parses XML files that contain the lines from Shakespeare’s plays,
then displays the name of the play as well as each act/scene every actor is in, for example,

Play  name: Tempest
Characters:
(stage_directions ): 1.1 1.2 2.1 2.2 3.1 3.2 3.3 4.1 5.1
Boatswain: 1.1 5.1
Alonso: 1.1 2.1 3.3 5.1
Gonzalo: 1.1  2.1 3.3 5.1

and so on...
"""

from bs4 import BeautifulSoup
from pytictoc import TicToc
from typing import TextIO
import sys

class LabTwo:

	def readFile(self, fileName: str) -> BeautifulSoup:
		
		try: # try to open provided input file, if successful: 

			with open(fileName, 'r') as f:
				soup = BeautifulSoup(f, 'lxml') # create BeautifulSoup object 'soup' with given file 
			
			return soup 

		except OSError:

			print('ERROR : cannot open ', fileName)
			return None


	def getPlayName(self, soup: BeautifulSoup) -> str:
		
		try: # try to retrieve and return 'name' attribute from the 'play' tag

			return soup.play['name']

		except: # no 'play' tag or 'name' attribute 

			print('Error: File Not Formatted correctly')
			return None
		 

	def getCharacters(self, soup: BeautifulSoup) -> dict:

		characters = {}  # Initialize an empty dictionary to store each character and their act/scene numbers

		scenes = soup.find_all('div', type='scene') # find and store all scenes in the play 

		for scene in scenes:

			act = scene.find_parent('div', type='act') # find the parent div, which will be the act of the scene
			actNum = act.get('n') # get act number
			sceneNum = scene.get('n') # get scene number

			chars = scene.find_all('sp') # find and store all characters in the scene

			for char in chars:
				
				charName = char.get('who')[1::] # get the name of the character, starts at index 1 because index 0 is a #
				
				if charName not in characters: # if the character is not already in the dictionary 

					characters[charName] = [] # initialize new key-value pair, the character name as the key and a empty list to store scene number as value

				if (actNum, sceneNum) not in characters[charName]: # if the character hasn't already appeared in the scene

					characters[charName].append((actNum, sceneNum)) # add the scene to the character's scene list

		return characters 


if __name__ == '__main__':
	#DO NOT MODIFY THIS CODE
	t = TicToc()
	t.tic() # start timer

	lab2 = LabTwo()
	f = lab2.readFile(sys.argv[1])
	if f:
		print('Play name:', lab2.getPlayName(f))
		print('Characters:')
		characters = lab2.getCharacters(f)
		if characters:
			for k,v in characters.items():
				
				print(k + ':', ''.join( [a + '.'+ b + ' ' for (a,b) in v] ) )

			print('*' * 13)

	t.toc() #elapsed time