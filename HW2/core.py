"""
PageRank Algorithm
"""
__author__="Utkarsh J"

from collections import defaultdict, OrderedDict
import itertools
import math
import pdb
import operator

IN_DICT = defaultdict(list) # default graph representation
OUT_DICT = defaultdict(int) # dictionary maintaining total unique outlinks
TOTALIL_DICT = defaultdict(int) # total inlink dictionary
PAGE_RANK = defaultdict(float) # Dictionary maintaining page ranks 
NEW_PAGE_RANK = defaultdict(float) # Dictionary maintaining temporary new page ranks
teleportation_factor = 0.85 
perplexity = [] # List maintaining perplexity 
sink_nodes =  [] # Sink nodes 

def get_outlinks():
	""" Gets page and generates hash for outlinks
	"""
	for page in IN_DICT.keys():
		OUT_DICT[page] = 0
	for page in IN_DICT.keys():
		for in_nodes in set(IN_DICT[page]): # set because we do not want duplicates
			OUT_DICT[in_nodes] += 1 

def get_perplexity():
	""" Calculates Perplexity for the current Page Ranks
	"""
	entropy = 0
	for page in PAGE_RANK.keys():
		entropy += PAGE_RANK[page]*math.log(1.0/PAGE_RANK[page],2)
	return 2 ** entropy

def is_converged():
	""" True if it converges , False otherwise
	"""
	first_diff = round(perplexity[-4]) 
	second_diff = round(perplexity[-3])
	third_diff = round(perplexity[-2])
	fourth_diff = round(perplexity[-1])
	return (first_diff == second_diff == third_diff == fourth_diff)

def main(file_path):
	"""
	Argument :
		file_path - path of file from which in link data is to be read
	"""
	# Read input and store it in adjacency list
	with open(file_path, 'r') as file_object:
		for line in file_object.readlines():
			in_elements =  line.strip().split(' ')
			# hashmap for in link dictionary
			# Approach 2 - remove self links 
			# if in_elements[0] in in_elements[1: ]:
			# 	temp_list = [x for x in in_elements[1:] if x != in_elements[0]]
			# else:
			temp_list = in_elements[1:]
			# this may contain duplicates
			IN_DICT[in_elements[0]] = temp_list

	# Calculate sources
	total_sources = 0
	for i in IN_DICT.keys():
		if len(IN_DICT[i]) == 0:
			total_sources += 1

	get_outlinks()

	# Calculate sinks
	for page in OUT_DICT:
		if OUT_DICT[page] == 0:
			sink_nodes.append(page)

	# Calculate total pages
	total_no_pages =  len(IN_DICT)

	# Assign initial page rank
	for page in IN_DICT.keys():
		PAGE_RANK[page] =  1.0/total_no_pages

	# FOR SMALL GRAPH GIVEN IN EXAMPLE
	# A D E F
	# B A F
	# C A B D
	# D B C
	# E B C D F
	# F A B D
	if file_path == "small_graph.txt":
		for i in range (1, 101):
			# calculate Sink PR
			sinkPR = 0
			for page in sink_nodes:
				sinkPR += PAGE_RANK[page]

			# teleportation and spread remaining sink PR evenly
			for page in IN_DICT.keys():
				NEW_PAGE_RANK[page] = (1.0 - teleportation_factor) / total_no_pages
				NEW_PAGE_RANK[page] += teleportation_factor * sinkPR / total_no_pages
				for in_node in IN_DICT[page]:			
					NEW_PAGE_RANK[page] += teleportation_factor * PAGE_RANK[in_node] / OUT_DICT[in_node]
			for page in IN_DICT.keys():
				PAGE_RANK[page] = NEW_PAGE_RANK[page]

			if i in [1, 10, 100]:
				with open('output_first.txt', 'a') as file_object:
					file_object.write('For ' + str(i) + '\n')
					for page in IN_DICT.keys():
						file_object.write('For ' + str(page) + ' page rank = ' + str(PAGE_RANK[page]) + '\n')
	else:
		def _should_continue():
			""" Checks if perplexity converges 
			"""
			if len(perplexity) < 5:
				return True
			else:
				return not is_converged()

		while(_should_continue()):
			# calculate Sink PR
			sinkPR = 0
			for page in sink_nodes:
				sinkPR += PAGE_RANK[page]

			# teleportation and spread remaining sink PR evenly
			for page, in_nodes in IN_DICT.iteritems():
				NEW_PAGE_RANK[page] = (1 - teleportation_factor) / total_no_pages
				NEW_PAGE_RANK[page] += teleportation_factor * sinkPR / total_no_pages
				for in_node in set(IN_DICT[page]):			
					NEW_PAGE_RANK[page] += teleportation_factor * PAGE_RANK[in_node]/ OUT_DICT[in_node]
			for page in IN_DICT.keys():
				PAGE_RANK[page] = NEW_PAGE_RANK[page]
			
			perplexity.append(get_perplexity())


		with open('output_second.txt', 'a') as file_object:
			file_object.write("a list of the perplexity values you obtain in each round until convergence \n")
			for value in perplexity:
				file_object.write(str(perplexity.index(value))+ " " + str(value) + "\n")

		with open('output_third.txt', 'a') as file_object:
			SortedPR = OrderedDict(sorted(PAGE_RANK.iteritems(), key=operator.itemgetter(1), reverse=True))
			file_object.write("A list of the document IDs of the top 50 pages as sorted by PageRank, together with their PageRank values \n")
			count = 1
			for page, value in SortedPR.items():
				file_object.write(str(count) + ". " + str(page) + " " + str(value) + "\n")
				count =  count + 1
				if count == 51:
					break

			file_object.write("\n\nA list of the document IDs of the top 50 pages as sorted by InLinks, together with their in links values \n")
			for page, value in IN_DICT.items():
				TOTALIL_DICT[page] = len(value)

			count = 1
			SortedIL = OrderedDict(sorted(TOTALIL_DICT.iteritems(), key=operator.itemgetter(1), reverse=True))
			for page, value in SortedIL.items():
				file_object.write(str(count) + ". " + str(page) + " " + str(value) + "\n")
				count  = count + 1
				if count == 51:
					break

			file_object.write("\n\n The proportion of pages with no in links\n")
			file_object.write("= " + str(total_sources) + "/" + str(total_no_pages) + " = " + str(float(total_sources)/float(total_no_pages)))

			file_object.write("\n\n The proportion of pages with no out links\n")
			file_object.write("= " + str(len(sink_nodes)) + "/" + str(total_no_pages) + " = " + str(float(len(sink_nodes))/float(total_no_pages)))

			initialPR = 1.0/total_no_pages
			temp_count = 0.0
			for page,value in PAGE_RANK.items():
				if value < initialPR:
					temp_count += 1
			
			file_object.write("\n\nthe proportion of pages whose PageRank is less than their initial uniform values \n")
			file_object.write("= " + str(temp_count) + "/" + str(total_no_pages) + " = " + str(temp_count/total_no_pages))

			print "in links of in links of WT21-B37-76"
			for in_links in IN_DICT['WT21-B37-76']:
				print len(IN_DICT[in_links])
				
main("small_graph.txt")
main('in_link.txt')