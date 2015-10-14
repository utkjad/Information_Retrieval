"""
PageRank Algorithm
"""
__author__="Utkarsh J"

from collections import defaultdict
import itertools

GRAPH_DICT = defaultdict(list)
PAGE_RANK = defaultdict(float)
teleportation_factor = 0.85

def main(file_path):
	"""
	Arguments:
		file_path - path of file from which in link data is to be read
	"""
	# Read input and store it in adjacency list
	with open(file_path, 'r') as file_object:
		for line in file_object:
			in_elements =  line.rstrip('\r\n').split()
			GRAPH_DICT[in_elements[0]] = in_elements[1: ]

	total_no_pages = float(len(GRAPH_DICT.keys()))

	# Assign initial page rank
	for page in GRAPH_DICT.keys():
		PAGE_RANK[page] =  1.0/total_no_pages
	for iteret in [1, 10, 100]:
		# Calculate total number of sink nodes
		total_no_sink_nodes = 0
		for page, in_nodes in GRAPH_DICT.items():
			if len(GRAPH_DICT[page]) == 0:
				total_no_sink_nodes += 1

		for i in range (0, iteret):
			# teleportation and spread remaining sink PR evenly
			for page, in_nodes in GRAPH_DICT.items():
				PAGE_RANK[page] = (1 - teleportation_factor) / total_no_pages
				PAGE_RANK[page] += (teleportation_factor * total_no_sink_nodes) / total_no_pages
				for in_node in GRAPH_DICT[page]:
					def _get_total_outlinks(node):
						outlinks = 0
						for page, in_node in GRAPH_DICT.items():
							if node in GRAPH_DICT[page]:
								outlinks += 1
						return outlinks				
					PAGE_RANK[page] += (teleportation_factor * PAGE_RANK[in_node])/ _get_total_outlinks(in_node)

		with open('output_first.txt', 'a') as file_object:
			file_object.write('For ' + str(iteret) + '\n')
			for page in GRAPH_DICT.keys():
				file_object.write('For ' + str(page) + ' page rank = ' + str(PAGE_RANK[page]) + '\n')




main('small_graph.txt')