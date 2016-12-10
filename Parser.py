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



spamprob01 = open('spamlist01.txt', 'w+')
safeprob01 = open('safelist01.txt', 'w+')
spamprob02 = open('spamlist02.txt', 'w+')
safeprob02 = open('safelist02.txt', 'w+')
results = open('results.txt','w')
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
ham_words = {}
corpus = {}

safe_words = {}
spam_words = {}
grineer = {}

#THIS IS THE STARTING PATH
#This function gets all the filenames that are inside the 'starting' directory
for dirname, dirnames, filenames in os.walk(args['starting']):
	for filename in filenames:
		fpath = os.path.join(dirname, filename)
		if "spmsga" in filename:
			#this adds to the total spam file count
			spm_mail01 += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in spam_words:
						ham_words[word] = 1
					else:
						ham_words[word] += 1
					spm_words01 += 1
		else:
			#This adds to the total safe mail count
			saf_mail01 += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in safe_words:
						safe_words01[word] = 1
					else:
						safe_words01[word] += 1
					saf_words01 += 1


for word, count in ham_words.items():
	prob = count / spm_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
	spamprob01.write(formation + '\n')

for word, count in safe_words01.items():
	prob = count / saf_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
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
	formation = "{0} " "  {1} {2}".format(str(word), str(count), str(result))
	spamprob02.write(formation + "\n")

for word, count in safe_words.items():
	prob = count / saf_words
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
	safeprob02.write(formation + "\n")


#COMPARISON
totals = spm_mail01 + saf_mail01
totalc = spm_mail + saf_mail

for value in ham_words:
	value.strip('('')')
	corpus[value] = ham_words[value]
	for value2 in spam_words:
		value2.strip('('')')
		grineer[value2] = spam_words[value2]
		for tech in corpus.items():
			for lancer in grineer.items():
				print(str(lancer))	



results.write("found a total of " + str(spm_words) + " in " + args['starting'] + " within spam emails\n")
results.write("found a total of " + str(saf_words) + " in " + args['classify'] + " within safe emails\n")
spamprob01.close()
safeprob01.close()
spamprob02.close()
safeprob02.close()
