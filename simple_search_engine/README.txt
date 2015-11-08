Utkarsh J.
Homework 3

Contents-
1. SYSTEM USED
2. FILES
3. HOW TO RUN THE PROGRAM
4. Description


1. SYSTEM USED-
Language - Python 2.7.6
OS - Ubuntu 14.04
Editor - Sublime text 3

2. FILES
	a) Source files -
		indexer.py - Python source file which generates inverted index
		bm25.py - Python source file which calculates BM25 ranking
	b) Serialization files
		number_of_tokens_json_dump  - file which contains term frequency dictionary ( { document_Id : term_frequency})
		index.txt - file which contains index dictionary i.e. {word: { doc_id : Term_frequency, ...},...}
	c) Given files 
		tccorpus.txt - corpus file
		queries.txt - file containing queries
	d) results.txt - Final file which contains top 100 documents with respect to BM25 ranking for all queries in queries.txt
	e) README.txt - This!
	f) index_visual_output.txt - file containing invertred index in human readable form (WORD (doc_id,term_frequency) doc_id,term_frequency) ...)

3. HOW TO RUN PROGRAM - 
	a) To get inverted index, run 
			python indexer.py tccorpus.txt index.txt
	b) To get BM25 index, run
			python bm25.py index.txt queries.txt 100 >results.txt

4. Description


