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


priorspam = open('spamlist.txt', 'w')
priorsafe = open('safelist.txt', 'w')
results = open('results.txt', 'a')

results.write("\n=========\n")

# Variables

spm_mail01 = 0 			#number of spam mail in prior files
saf_mail01 = 0 			#number of safe mail in prior files
dspm_mail = 0 			#actual number of spam mail in to-classify files
dsaf_mail = 0			#actual number of safe mail in to-classify files
cspm_mail = 0			#detected number of spam mail in to-classify files
csaf_mail = 0			#detected number of safe mail in to-classify files
sspm_mail = 0			#detected number of mail that are spam but are classified as safe
ssaf_mail = 0			#detected number of mail that are safe but are classified as spam

spm_words01 = 0			#total number of words within spam mail in prior files
saf_words01 = 0			#total number of words within safe mail in prior files

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
results.write("filepaths of sources:\n")
for source in sources:
	results.write(str(source) + "\n")
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
							spam_words.append(word)
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
							safe_words.append(word)
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
	priorspam.write(formation + '\n')
	ham_probability[word] = prob

for word, count in safe_wordcount.items():
	prob = count / saf_words01
	result = '{:1.10f}'.format(prob)
	formation = "{0} " " {1} {2}".format(str(word), str(count), str(result))
	priorsafe.write(formation + '\n')
	safe_probability[word] = prob

priorspam.close()
priorsafe.close()

#pre-bayes classifier computations
spamclass_prob = spm_mail01 / (spm_mail01 + saf_mail01)						#P(spam)
safeclass_prob = saf_mail01 / (spm_mail01 + saf_mail01)						#P(safe)
results.write("P(spam) = " + '{:1.10f}'.format(spamclass_prob) + "\n")
results.write("P(safe) = " + '{:1.10f}'.format(safeclass_prob) + "\n\n")

# THIS IS THE CLASSIFIER PATH
results.write("classifying results:\n")
for files in toclass:
	for dirname, dirnames, filenames in os.walk(files):
		for filename in filenames:
			results.write(str(filename) + "\n")
			wordcount = {}			#dictionary of words found within the text; format 'word' - 5
			total = 0				#total number of words found within the text w/o repetition
			gtotal = 0				#total number of words found within the text w/ repetition
			words = []
			gpath = os.path.join(dirname, filename)
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
							gtotal += 1
				results.write("total # of words w/o repetiton: " + str(total) + "\n")
				results.write("total # of words w/ repetition: " + str(gtotal) + "\n")
				#computing probability
				spam_prob = spamclass_prob
				safe_prob = safeclass_prob
				zerospam = 0  #number of words that did not exist as spam word
				zerosafe = 0  #number of words that did not exist as safe word
				for word, count in wordcount.items():
						if word in spam_words:
							spam_prob *= (count+1) / (spm_mail01+(total*2))
							# wordcount[word] += 1
						else:
							spam_prob *= 1 / (spm_mail01+(total*2))
							# wordcount[word] = 1
							zerospam += 1
				for word, count in wordcount.items():
					if word in safe_words:
						safe_prob *= (count+1) / (saf_mail01+(total*2))
						# wordcount[word] += 1
					else:
						safe_prob *= 1 / (saf_mail01+(total*2))
						# wordcount[word] = 1
						zerosafe += 1

				# spam_prob *= spamclass_prob
				results.write("P(" + str(filename) + "|spam) = " + '{:1.20f}'.format(spam_prob) + "\n")
				# safe_prob *= safeclass_prob
				results.write("P(" + str(filename) + "|safe) = " + '{:1.20f}'.format(safe_prob) + "\n")
				if spam_prob > safe_prob:
					cspm_mail += 1
					results.write("it is spam\n")
				if safe_prob >= spam_prob:
					sspm_mail += 1
					results.write("it is safe\n")				
				results.write("number of words with zero probability in spam list: " + str(zerospam) + "\n")
				results.write("number of words with zero probability in safe list: " + str(zerosafe) + "\n")
				results.write("\n")
			else:
				dsaf_mail += 1
				g = open(gpath)
				for line2 in g:
					for word in g.read().split():
						if word not in words:
							wordcount[word] = 1
							total += 1
						else:
							wordcount[word] += 1
							gtotal += 1
				results.write("total # of words w/o repetiton: " + str(total) + "\n")
				results.write("total # of words w/ repetition: " + str(gtotal) + "\n")
				#computing probability
				spam_prob = spamclass_prob
				safe_prob = safeclass_prob
				zerospam = 0  #number of words that did not exist as spam word
				zerosafe = 0  #number of words that did not exist as safe word
				for word, count in wordcount.items():
						if word in spam_words:
							spam_prob *= (count+1) / (spm_mail01+(total*2))
							# wordcount[word] += 1
						else:
							spam_prob *= 1 / (spm_mail01+(total*2))
							# wordcount[word] = 1
							zerospam += 1
				for word, count in wordcount.items():
					if word in safe_words:
						safe_prob *= (count+1) / (saf_mail01+(total*2))
						# wordcount[word] += 1
					else:
						safe_prob *= 1 / (saf_mail01+(total*2))
						# wordcount[word] = 1
						zerosafe += 1

				# spam_prob *= spamclass_prob
				results.write("P(" + str(filename) + "|spam) = " + '{:1.20f}'.format(spam_prob) + "\n")
				# safe_prob *= safeclass_prob
				results.write("P(" + str(filename) + "|safe) = " + '{:1.20f}'.format(safe_prob) + "\n")
				if spam_prob > safe_prob:
					ssaf_mail += 1
					results.write("it is spam\n")
				if safe_prob >= spam_prob:
					csaf_mail += 1
					results.write("it is safe\n")
				results.write("number of words with zero probability in spam list: " + str(zerospam) + "\n")
				results.write("number of words with zero probability in safe list: " + str(zerosafe) + "\n")
				results.write("\n")

# results.write("found a total of " + str(spm_words01) + " in " + args['starting'] + " within spam emails\n")
# results.write("found a total of " + str(saf_words01) + " in " + args['starting'] + " within safe emails\n")
print("found a total of " + str(spm_words01) + " in " + args['starting'] + " within spam emails\n")
print("found a total of " + str(saf_words01) + " in " + args['starting'] + " within safe emails\n")
print("classified a total of " + str(cspm_mail) + "in" + args['classify'] + " within " + str(dspm_mail) + " spam emails\n")
print("classified a total of " + str(csaf_mail) + "in" + args['classify'] + " within " + str(dsaf_mail) + " safe emails\n")
results.write("actual number of spam mails: " + str(dspm_mail) + "\n")
results.write("classified number of spam mails: " + str(cspm_mail) + "\n")
results.write("missed number of spam mails: " + str(sspm_mail) + "\n")
results.write("actual number of safe mails: " + str(dsaf_mail) + "\n")
results.write("classified number of safe mails: " + str(csaf_mail) + "\n")
results.write("missed number of safe mails: " + str(ssaf_mail) + "\n")
results.write("classified a total of " + str(cspm_mail) + "in" + args['classify'] + " within " + str(dspm_mail) + " spam emails\n")
results.write("spam classifying accuracy: " + '{:1.10f}'.format((cspm_mail/dspm_mail)*100) + "\n")
results.write("classified a total of " + str(csaf_mail) + "in" + args['classify'] + " within " + str(dsaf_mail) + " safe emails\n")
results.write("safe classifying accuracy: " + '{:1.10f}'.format((csaf_mail/dsaf_mail)*100) + "\n")
results.close()