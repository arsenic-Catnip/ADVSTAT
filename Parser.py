# created by marienne lopez & charles ambas
# run this in cmd as : parser.py -s "C:/file/path/"
# 	where it will generate two text files
#	that contain the probabilities of all words
#	found in two kinds of emails

# IMPORTS
import argparse
import os
import sys

# constructing argument parse 
# run this in cmd as : parser.py -s "C:/file/path/" -c "C:/file/path/"
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--starting", required=True, 
	help="starting folder location to extract folders; indicate multiple paths with comma")
ap.add_argument("-c", "--classify", required=True, 
	help="starting folder location to extract folders; indicate multiple paths with comma")
args = vars(ap.parse_args())
sources = sys.argv[2].split(',')
toclass = sys.argv[4].split(',')


spamprob01 = open('spamlist01.txt', 'w+')
safeprob01 = open('safelist01.txt', 'w+')
# spamprob02 = open('spamlist02.txt', 'w+')
# safeprob02 = open('safelist02.txt', 'w+')
# results = open('results.txt','w')
# same = open('same.txt', 'w')
# Variables

spm_mail01 = 0 			#number of spam mail in prior files
saf_mail01 = 0 			#number of safe mail in prior files
dspm_mail = 0 			#actual number of spam mail in to-classify files
dsaf_mail = 0			#actual number of safe mail in to-classify files
cspm_mail = 0			#detected number of spam mail in to-classify files
csaf_mail = 0			#detected number of safe mail in to-classify files

spm_words01 = 0			#total number of words within spam mail in prior files
saf_words01 = 0			#total number of words within safe mail in prior files
# spm_words = 0			#total number of words within spam mail in to-classify files
# saf_words = 0			#total number of words within safe mail in to-classify files

safe_wordcount = {}		#dictionary of safe words with their word count in prior files; format 'word' - 5
ham_wordcount = {}		#dictionary of spam words with their word count in prior files; format 'word' - 5
safe_probability = {} 	#dictionary of safe words with their probability in prior files; format 'word' - 0.5
ham_probability = {}	#dictionary of spam words with their probability in prior files; format 'word' - 0.5
safe_words = []
spam_words = []

# corpus = {}			
# grineer = {}		

#THIS IS THE STARTING PATH
#This function gets all the filenames that are inside the 'starting' directory
#extracting apriori information from spam and safe mails
for source in sources:
	for dirname, dirnames, filenames in os.walk(source):
		for filename in filenames:
			fpath = os.path.join(dirname, filename)
			if "spmsg" in filename:
				#this adds to the total spam file count
				spm_mail01 += 1
				f = open(fpath)
				for line in f:
					for word in f.read().split():
						if word not in spam_words:
							ham_wordcount[word] = 1
						else:
							ham_wordcount[word] += 1
						spm_words01 += 1
			else:
				#This adds to the total safe mail count
				saf_mail01 += 1
				f = open(fpath)
				for line in f:
					for word in f.read().split():
						if word not in safe_words:
							safe_wordcount[word] = 1
						else:
							safe_wordcount[word] += 1
						saf_words01 += 1

# alltotal = spm_words01	#total number of words overall, no repetitions
# for word in safe_words:
# 	if word not in spam_words:
# 		alltotal += 1

for word, count in ham_wordcount.items():
	prob = count / spm_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
	spamprob01.write(formation + '\n')
	ham_probability[word] = prob

for word, count in safe_wordcount.items():
	prob = count / saf_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
	safeprob01.write(formation + '\n')
	safe_probability[word] = prob

#pre-bayes classifier computations
spamclass_prob = spm_mail01 / (spm_mail01 + saf_mail01)						#P(spam)
safeclass_prob = saf_words01 / (spm_mail01 + saf_mail01)					#P(safe)

# THIS IS THE CLASSIFIER PATH
for files in toclass:
	for dirname, dirnames, filenames in os.walk(files):
		for filename in filenames:
			gpath = os.path.join(dirname, filename)
			wordcount = {}			#dictionary of words found within the text; format 'word' - 5
			total = 0				#total number of words found within the text w/o repetition
			words = []
			if "spmsg" in filename:
				dspm_mail += 1
				g = open(gpath)
				for line2 in g:
					for word in g.read().split():
						if word not in words:
							wordcount[word] = 1
							total += 1
						else:
							wordcount[word] += 1
			else:
				dsaf_mail += 1
				g = open(gpath)
				for line2 in g:
					for word in g.read().split():
						if word not in words:
							wordcount[word] = 1
						else:
							wordcount[word] += 1
						total += 1

			#computing probability
			spam_prob = 1
			safe_prob = 1
			for word, count in wordcount.items():
					if word in spam_words:
						spam_prob *= (count+1) / (spm_mail01+total)
					else:
						spam_prob *= 1 / (spm_mail01+total)
			for word, count in wordcount.items():
				if word in safe_words:
					safe_prob *= (count+1) / (saf_mail01+total)
				else:
					safe_prob *= 1 / (saf_mail01+total)
			spam_prob *= spamclass_prob
			safe_prob += safeclass_prob
			if spam_prob > safe_prob:
				cspm_mail += 1
			else:
				csaf_mail += 1

# results.write("found a total of " + str(spm_words01) + " in " + args['starting'] + " within spam emails\n")
# results.write("found a total of " + str(saf_words01) + " in " + args['starting'] + " within safe emails\n")
spamprob01.close()
safeprob01.close()
print("found a total of " + str(spm_words01) + " in " + args['starting'] + " within spam emails\n")
print("found a total of " + str(saf_words01) + " in " + args['starting'] + " within safe emails\n")
print("classified a total of " + str(cspm_mail) + "in" + args['classify'] + " within " + str(dspm_mail) + " spam emails\n")
print("classified a total of " + str(csaf_mail) + "in" + args['classify'] + " within " + str(dsaf_mail) + " safe emails\n")
