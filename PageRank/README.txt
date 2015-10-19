HW2

Contents-
1. SYSTEM USED
2. FILES
4. HOW TO RUN THE PROGRAM

1. SYSTEM USED-
Language - Python 2.7.6
OS - Ubuntu 14.04

2. FILES
small_graph.txt - File containing given example of graph in HW2
in_link.txt - in­links file for the WT2g
output_first.txt -  page rank values for iterations 1, 10, 100
output_second.txt -  contains perplexity values till it converges 
output_third.txt -  contains following-
			- a list of the document IDs of the top 50 pages as sorted by PageRank, together with their PageRank values;
			- a list of the document IDs of the top 50 pages by in­link count, together with their in­link counts;
			- the proportion of pages with no in­links (sources);
			- the proportion of pages with no out­links (sinks)
			- the proportion of pages whose PageRank is less than their initial, uniform values.
fourth_deliverable.pdf -  Analysis of Page Rank implementation 

3. HOW TO RUN PROGRAM - 
code is in the file core.py
go to directory containing core.py
run 
`python core.py`

