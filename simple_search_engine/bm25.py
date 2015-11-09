# BM25 implementation
import json
import math
import operator
from collections import defaultdict, OrderedDict, Counter
import sys

# index_file = 'index_json_dump.txt'
number_of_tokens_file = "number_of_tokens_json_dump"

# queries_file = 'queries.txt'
result_file = 'result.txt'

# load index and number of tokens
number_of_tokens = json.load(open(number_of_tokens_file))
index = json.load(open(sys.argv[1]))

# calculate avdl
N = len(number_of_tokens)
avdl = float(sum(x['dl'] for x in number_of_tokens.values())) / N

query_freq = defaultdict(int)
bm25 = defaultdict(float)
			
k1 = 1.2 
k2 = 100.00
b = 0.75

def bm25_run():
	
	index_file = sys.argv[1]
	queries_file = sys.argv[2]
	limit = int(sys.argv[3])

	with open(queries_file, 'r') as query_file_obj:
		# calculate query frequency 
		query_id = 1
		for query_line in query_file_obj.readlines():
			query = query_line.split()
			for term in query:
				query_freq[term] += 1
			# for each term
			for term in query_freq:
				# calculate ni
				ni = len(index[term])
				# calculate BM25 for each doc 
				for doc_id,tf in index[term].iteritems():
					# calculate k
					k = k1*((1-b) + (b* (number_of_tokens[doc_id]['dl'] / avdl)))
					term1 =  (N - ni + 0.5) / (ni + 0.5)
					term2 =  ((k1 + 1) * tf) / (k + tf)
					term3 =  ((k2 + 1) * query_freq[term]) / (k2 + query_freq[term])
					global bm25
					bm25[doc_id] += math.log(term1)*term2*term3

			# dump first 100 results in results.txt
			#with open(result_file, 'wb') as file_object:
			# get first 100 results
			# sorted_index = OrderedDict(sorted(bm25.iteritems(), key=operator.itemgetter(1), reverse=True))
			# sorted_index_100 = Counter(bm25).most_common(100)

			sorted_index_list = sorted(bm25.iteritems(), key=operator.itemgetter(1), reverse=True)[:limit]

			rank = 1
			for doc,bm25o in sorted_index_list:
				print(str(query_id) + " Q0 " + str(doc) + " " + str(rank)  + " " +  str(bm25o) + " utkjad" )
				rank += 1
				
			query_id += 1
			query_freq.clear()

bm25_run()