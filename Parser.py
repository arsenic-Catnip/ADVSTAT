# created by marienne lopez & charles ambas
# run this in cmd as : parser.py -s "C:/file/path/"
# 	where it will generate two text files
#	that contain the probabilities of all words
#	found in two kinds of emails

# IMPORTS
import argparse
import os

# constructing argument parse 
# run this in cmd as : parser.py -s "C:/file/path/"
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--starting", required=True, 
	help="starting folder location to extract folders")
ap.add_argument("-c", "--classify", required=True, 
	help="starting folder location to extract folders")
args = vars(ap.parse_args())



spamprob01 = open('spamlist01.txt', 'r+')
safeprob01 = open('safelist01.txt', 'r+')
spamprob02 = open('spamlist02.txt', 'r+')
safeprob02 = open('safelist02.txt', 'r+')
same = open('same.txt', 'w')
# Variables



spm_mail01 = 0
saf_mail01 = 0
spm_mail = 0
saf_mail = 0

spm_words01 = 0
saf_words01 = 0
spm_words = 0
saf_words = 0

safe_words01 = {}
spam_words01 = {}
safe_words = {}
spam_words = {}

#THIS IS THE STARTING PATH
for dirname, dirnames, filenames in os.walk(args['starting']):
	for filename in filenames:
		fpath = os.path.join(dirname, filename)
		if "spmsga" in filename:
			spm_mail01 += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in spam_words:
						spam_words01[word] = 1
					else:
						spam_words01[word] += 1
					spm_words01 += 1
		else:
			saf_mail01 += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in safe_words:
						safe_words01[word] = 1
					else:
						safe_words01[word] += 1
					saf_words01 += 1

for word, count in spam_words01.items():
	prob = count / spm_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	spamprob01.write(formation + '\n')

for word, count in safe_words01.items():
	prob = count / saf_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	safeprob01.write(formation + '\n')



# THIS IS THE CLASSIFIER PATH
for dirname, dirnames, filenames in os.walk(args['classify']):
	for filename in filenames:
		gpath = os.path.join(dirname, filename)
		if "spmsga" in filename:
			spm_mail01 += 1
			g = open(gpath)
			for line2 in g:
				for word in g.read().split():
					if word not in spam_words:
						spam_words[word] = 1
					else:
						spam_words[word] += 1
					spm_words += 1
		else:
			saf_mail01 += 1
			g = open(gpath)
			for line2 in g:
				for word in g.read().split():
					if word not in safe_words:
						safe_words[word] = 1
					else:
						safe_words[word] += 1
					saf_words += 1

for word, count in spam_words.items():
	prob = count / spm_words
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	spamprob02.write(formation + '\n')

for word, count in safe_words.items():
	prob = count / saf_words
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	safeprob02.write(formation + '\n')
#COMPARISON Still doesn't work :/
filespam1 = spamprob01.read().split(None, 1)
filespam2 = spamprob02.read().split(None, 1)
file1 = safeprob01.read().split(None, 1)
file2 = safeprob02.read().split(None, 1)


for f2 in filespam1:
	for f3 in filespam2:
		if f2 in f3:
			same.write(f2)
for f4 in file1:
	for f5 in file2:
		if f4 in f5:
			same.write(f4)




print("found a total of " + str(spm_words) + " in " + args['starting'] + " within spam emails\n")
print("found a total of " + str(saf_words) + " in " + args['starting'] + " within safe emails\n")
spamprob01.close()
safeprob01.close()
spamprob02.close()
safeprob02.close()
