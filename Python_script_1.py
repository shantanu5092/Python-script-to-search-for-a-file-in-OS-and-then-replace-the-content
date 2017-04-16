# This Python script finds a file path with only the file name and then replaces a particular word with a string in that file as many number of times as it appears.

#!/usr/bin/Python

# The above line is to set the interpreter and is not treated as a comment because of ! along with #

# print 'Hello World'

import os

from os.path import join 									# os.path is a part of sys.modules and not the os module. However it plays some trick. Consider "os.path" as a module itself

import re											# This will allow us to use regular expressions

import sys											# This import statement is used to write to the file using sys.stdout statement

#from docx import document									# This is used when dealing with word files.

flag_g = 0

file_path_g = ""

def find(file_name_l1):										# Note that file_name_l is coming from the user input.

	global flag_g										# for using global variables in functions that modify their values you need to define them global
	global file_path_g
	
	for root, dir, files in os.walk('/Users'):						# this line yields 3 tuples, typical syntax for os.walk
		#print "searching"
		if file_name_l1 in files:
			flag_g = 1
			file_path_g = root # + "/" + file_name_l1
			break
			
	if flag_g == 1: 
		print "Search successful, file exists \n"
		locate_l = raw_input("Do you want to locate the file? Y/N \n")
		if(locate_l == 'Y'):
			print file_path_g
			
	else: 
		print "File not found"
		

def edit(file_name_l2, file_path_g):

	outline = []										# List declaration for storing the changed values that will be mapped to the original file later on.

	if (flag_g!=0):										# You don't want to edit the document if file does not exist
		make_change_l = raw_input("Do you want to edit the document? Y/N \n")
	
		if(make_change_l == 'Y'):
			os.chdir(file_path_g)
			
			# print os.getcwd()							# used for checking the functionality
			# print file_name_l2							# used for checking the functionality
			
			# open_file = open(file_name_l2, 'r+')					# the file is now opened. And we will use regular expression to find or match a particular string
			
			# document = Document(open_file)					# This is used when dealing with word files
			
			# count the number of occurrences of "timing" in "sv.docx"
			
			count = 0
			count1 = 0

			#lines = open_file.readline()
			
			word1 = raw_input("Enter the string you want to search for \n")
			
			word2 = raw_input("Enter the string you want to replace the above string with \n")
			
			with open(file_name_l2, 'r+') as open_file:
				for abc in open_file:
					count += 1
					if word1 in abc:
						count1 += 1
						abc = abc.replace(word1, word2)
						outline.append(abc)
						
					else:
						outline.append(abc)
			
			#print outline								# used for checking the functionality
			#print count								# used for checking the functionality
			#print count1								# used for checking the functionality
						
			orig_stdout = sys.stdout						# This is used to redirect the stdout so that it does not get buffered and print function can work properly
			
			f = open(file_name_l2, 'w')
			
			sys.stdout = f
			
			for item in outline:
				sys.stdout.write(item)
				#print>>open_file, item						
				#the_file.write("%s\n", item)					# Never use .write function for replacing the content. It will always overwrite the existing file.
				
			sys.stdout = orig_stdout
			
			f.close()
			
			print "Conversion successful"
			
		else:
			print "Program exiting..."	
			
			
			
############ This is some practise garbage code that didn't work################################################
			#with open(file_name_l2, 'w+') as open_file_2:
			#	for xyz in outline:
			#		open_file_2.write(xyz)
			
		
					#if word in line:
						#open(file_name_l2, 'a').write(re.sub(word, 'papaji', word, re.I ))
						#open(file_name_l2, 'w').write(re.sub(word, 'hello', word))
				
				
				#lines = open_file.readline()
				#for line in open_file:
				#	count1 = count1 + 1
				#	if word in re.search():
				#		count += 1
				
			
			#while(lines!=$):
			#	lines = open_file.readline()
			#	count1 = count1 + 1
			
			#for abc in lines:
			#	if word in abc:
			#		count = count + 1

			
			#open_file.close()							# The files is now closed.
			
##################################################################################################################
		

def open_resume():
	
	file_name_l2 = raw_input("Enter the name of the file you want to search \n ")
	
	print "searching for the file " + '"' + file_name_l2 + '"' + "..."			# This is how you would include the user input into quotes.
	
	find(file_name_l2)
	
	edit(file_name_l2, file_path_g)
	
	
	
open_resume()
