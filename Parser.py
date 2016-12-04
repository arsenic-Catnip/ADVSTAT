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
args = vars(ap.parse_args())

# problist = open('problist.txt', 'w')

spamprob = open('spamlist.txt', 'w')
safeprob = open('safelist.txt', 'w')

# Variables
spm_mail = 0
saf_mail = 0
spm_words = 0
saf_words = 0
safe_words = {}
spam_words = {}
# list = {}

for dirname, dirnames, filenames in os.walk(args['starting']):
	for filename in filenames:
		fpath = os.path.join(dirname, filename)
		if "spmsga" in filename:
			spm_mail += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in spam_words:
						spam_words[word] = 1
					else:
						spam_words[word] += 1
					spm_words += 1
		else:
			saf_mail += 1
			f = open(fpath)
			for line in f:
				for word in f.read().split():
					if word not in safe_words:
						safe_words[word] = 1
					else:
						safe_words[word] += 1
					saf_words += 1

for word, count in spam_words.items():
	# problist.write(str(word) + " " + str(count) + "\n")
	prob = count / spm_words
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	spamprob.write(formation + '\n')

for word, count in safe_words.items():
	# problist.write(str(word) + " " + str(count) + "\n")
	prob = count / saf_words
	result = '{:1.10f}'.format(prob)
	formation = "{0} {1} {2}".format(str(word), str(count), str(result))
	safeprob.write(formation + '\n')


print("found a total of " + str(spm_words) + " in " + args['starting'] + " within spam emails\n")
print("found a total of " + str(saf_words) + " in " + args['starting'] + " within safe emails\n")
spamprob.close()
safeprob.close()
