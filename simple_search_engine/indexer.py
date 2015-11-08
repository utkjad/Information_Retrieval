"""
Building inverted index 
"""

__author__  = "Utkarsh J"

import re
import sys
import json
from collections import defaultdict

doc_multi_regex = re.compile("^#\\s*[0-9]+$")

index = defaultdict(lambda: defaultdict(int))
# Dictionary { Word : { doc_id : tf, doc_id : tf, doc_id : tf},
#				 Word : { doc_id : tf, doc_id : tf, doc_id : tf}}

number_of_tokens = defaultdict(lambda: defaultdict(int))
# Dictionary
# 			{doc_id : term frequency }

#default test values
# corpus_file = "tccorpus.txt"
# index_file = "index.txt"

# json dump files
number_of_tokens_json_dump = 'number_of_tokens_json_dump'
index_visual_output = 'index_visual_output.txt'

def calculate_inverted_index():
	# Get corpus file and index file from command line 
	corpus_file = sys.argv[1]
	index_file = sys.argv[2]
	
	# For all queries 
	with open(corpus_file, 'r') as file_object:
		for line in file_object.readlines():
			# line is document number
			if doc_multi_regex.match(line):
				document_number = line.split()[-1]
			elif document_number:
				for word in filter(lambda x: not x.isdigit(), line.split()):
					index[word.lower()][document_number] += 1
					number_of_tokens[document_number]['dl'] += 1

	# Dump index Hash
	with open(index_file, 'w') as file_object:
		file_object.write(json.dumps(index))

	# Dump number of tokens tf
	with open(number_of_tokens_json_dump, 'w') as file_object:
		file_object.write(json.dumps(number_of_tokens))

	# Output in following format (Display purspose only)
	# word (doc_id, tf) (doc_id, tf) (doc_id, tf) (doc_id, tf)
	with open(index_visual_output, 'w') as file_object:
		for word,value in index.iteritems():
			file_object.write(word + " ")
			for doc_id, tf in value.iteritems():
				file_object.write("(" + str(doc_id) + "," + str(tf) + ") ")
			file_object.write("\n")
			
calculate_inverted_index()