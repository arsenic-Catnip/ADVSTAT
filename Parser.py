# created by marienne lopez
# this extracts all the words given a folder 
# run this in cmd as : parser.py -s "C:/file/path/"
# 	where it will create a text file containing a list
#   of all text files

import argparse
import os
import re

# constructing argument parse
# when running this file type "python filechecker.py -s file1 -c file2" in cmd 
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--starting", required=True, 
	help="starting folder location to extract folders")
args = vars(ap.parse_args())


word_results = open('wordresults.txt', 'a')
word_results.write('-------------\n')
word_results.write('wordlist of documents found in' + args['starting'] + '\n')
# results = open('filelist.txt', 'a')
# results.write('-------------\n')
# results.write('filelist of ' + args['starting'] + '\n')
files = 0
for dirname, dirnames, filenames in os.walk(args['starting']):

	for filename in filenames:
		#print(os.path.join(dirname, filename))
			# results.write(os.path.join(dirname, subdirname) + '\n')
		if filename.endswith('.txt'):
			# results.write(os.sep.join([dirname, filename])+ '\n')
			fpath = os.path.join(dirname, filename)
			word_results.write('-------------\n')
			word_results.write("wordlist of " + fpath + ": \n")
			f = open(fpath)
			for line in f:
				# print(line)
				list = line.split()
				for word in list:
					word_results.write(str(word) + "\n")
			# content = f.read()
			# word_results.write(content + "\n")
			files = files+1
                                        
print('Successfully found '+ str(files) + ' files in '+ args['starting'])
# results.write('# of files found'+ str(files))
# print('Words found in the documents: ' + '' + str(content))
