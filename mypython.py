#!/bin/python3
#*******************************************************************************
# Author:	Sarah Harber
# Update Date:	7/28/17
# Program Name:	myPtyhon
# Description:  A simple python program to that will do the following:
#			1.) Create 3 files.
# 			    - Files will be contained in the current 
#				  directory.
#			2.) Randomly generate a string in each file.
#			    - String must contain 10 random letters.
#			    - Letters must all be lowercase characters.
#			    - String should not contain any spaces.
#			    - The 11th Character must be a newline character.
#			3.) Print out contents of all 3 files to the string.
#			4.) Print out 2 Random Integers.
#			    - Integers Range is 1 to 42, inclusive. 
#			5.) Print out the Product of the integers created in 
#			    step 4.
#*******************************************************************************

# Import Needed Functions
import string, random
from random import randint

# Declare all file names in a variable.
fileName1 = "File_1"
fileName2 = "File_2"
fileName3 = "File_3"


# Create a function to  write a random string to the  file.
#**************************************************************************************
# Function: 	writeRandomString
# Description: 	Function will open/create a file with the name of the string passed 
#		to it, generate a random string, write the string and a new line char
#		to the file, close the file.  Then the function will open the file
#		and read the contents to the terminal.
#**************************************************************************************
def writeRandomString(nameFile):
	fileName = open(nameFile, "w")	# Open/Create a file to write
	tempString = ""	#Reset Temp String.
	tempString ="".join(random.choice(string.ascii_lowercase) for x in range(10))
	fileName.write(tempString + "\n") # Write tempString to file.
	fileName.close() # Close the File
	tempFile = open(nameFile, "r") # Open the file
	myString = tempFile.read() # Read the contents & store in myString
	print(myString) # Print the contents to the terminal.
	tempFile.close() # Close the File.
	return 
#***************************************************************************************

# Use function to get random string written to each file.
writeRandomString(fileName1)
writeRandomString(fileName2)
writeRandomString(fileName3)


# Get two random integers between 1 & 42.
randInt1 = randint(1,42)
randInt2 = randint(1,42)

# Print the two random integers to the screen
print(randInt1)
print(randInt2)

# Calculate the Product of randInt1 & randInt2
product = randInt1 * randInt2

# Print the product to the screen
print(product)
