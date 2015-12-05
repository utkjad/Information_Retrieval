Utkarsh J.
Homework 5

Contents-
1. SYSTEM USED
2. FILES
3. HOW TO RUN THE PROGRAM
4. Precision @ 20 values 
5. MAP 


NOTE - the part where MAP and Precision @ 20 are commented as of now in the code. If you want to run the program and 
see the MAP and precision @ 20 for individual querries, you can do so by uncommenting it.
Also, values in part 5 are observed when the program is run keeping the lines uncommented!

1. SYSTEM USED-
Language - Python 2.7.6
OS - Ubuntu 14.04
Editor - Sublime text 3/ PyCharm

2. FILES
	a) Source files -
		core.py - Python source file implementing the required measures
	b) Input files from HW4 - (Files wrt query)
		portable_operating_systems.txt 
		code_optimization_for_space_efficiency.txt
		parallel_algorithms.txt
	c) Relevance file
		relevance.txt 
	d) results.txt - 
		Contains results form for all three given queries, and prints following attributes-
			Name of the Query and Query ID 
				Rank
				Document ID
				Document score
				Relevance level
				Precision
				Recall
		It also prints Precision @ 20 after each query
		It also prints MAP at the end 
	e) README.txt - This!
	
3. HOW TO RUN PROGRAM - 
	python core.py > results.txt

4. Precision @ 20
	For Query ID 12 - precision at 20 = 0.2
	For Query ID 13 - precision at 20 = 0.2
	For Query ID 19 - precision at 20 = 0.35

5. MAP = 0.433261712221
