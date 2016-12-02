# created by marienne lopez
# this extracts all the words given a folder 
# run this in cmd as : parser.py -s "C:/file/path/"
# 	where it will create a text file containing a list
#   of all text files

# IMPORTS
import argparse
import os

# constructing argument parse
# when running this file type "python filechecker.py -s file1 -c file2" in cmd 
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--starting", required=True, 
	help="starting folder location to extract folders")
args = vars(ap.parse_args())

spamprob = open('spams2x.txt', 'w')
normpron = open('normies.txt', 'w')

# Variables
spam_files = 0
normals = 0
word_count = 0
word_prob = {}
spam = 0
notspam = 0
pattern = 'spmsga*.txt'

for dirname, dirnames, filenames in os.walk(args['starting']):
	for filename in filenames:
		fpath = os.path.join(dirname, filename)
		if "spmsga" in filename:
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))

						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						spamprob.write(formation + "\n")
						#test_results.write(str(vocaloid)
				spam_files = spam_files+1

		elif "1-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
				normals = normals + 1
		elif "2-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "3-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "4-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_coun
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "5-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "6-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "7-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "8-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")
						
				normals = normals + 1
		elif "9-" in filename:
			fpath = os.path.join(dirname, filename)
			f = open(fpath)

			#WORD COUNTING PER  AS IT READS
			for line in f:
				wordcount = {}
				list = line.split()
				for word in list:
					#word_results.write(str(word) + "\n")
					for words in f.read().split():	
						if words not in wordcount:
							wordcount[words] = 1
							word_count += 1 
						else:
							wordcount[words] += 1
	
					for hatsune, miku in wordcount.items():
						word_prob = miku / word_count
						result = '{0:.3g}'.format(word_prob)
						formation = "{0}  Count: {1} Likelihood: {2} ".format(str(hatsune), str(miku), str(result))
						
						print(str(hatsune),str(miku) + ' - Likelihood = ' + str(result))
						normpron.write(formation + "\n")						
				normals = normals + 1
							
                                        
	print('Successfully found '+ str(spam_files) + ' spam files in '+ args['starting'])
	print('Successfully found '+ str(normals) + ' files in '+ args['starting'])
# results.write('# of files found'+ str(files))
# print('Words found in the documents: ' + '' + str(content))
