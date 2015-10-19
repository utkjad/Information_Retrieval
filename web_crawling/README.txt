HW1

Contents-
1. SYSTEM USED
2. FILES
3. HOW TO INSTALL LIBRARIES
4. HOW TO RUN THE PROGRAM
5. RESULTS

1. SYSTEM USED-
Language - Python 2.7.6
Libraries - BeautifulSoup, requests
OS - Ubuntu 14.04

2. FILES - 
I. core.py - contains Python program
II. first_output - list of the pages crawled when the crawler is run with no keyphrase, in other words all Wikipedia pages  meeting the requirements above to a depth of 5 from the starting seed
III. second_output - list of the pages crawled when the keyphrase is ‘concordance’

3. HOW TO INSTALL LIBRARIES
Instructions-
1. For BeautifulSoup, run `$ apt-get install python-bs4`
2. For requests, run `$ pip install requests`

4. HOW TO RUN THE PROGRAM
1. In the directory ~/HW1/ run `python core.py`

4. RESULTS:
The proportion is -> URLs with word "concordance" divided by total URLs crawled
which is 551/24620 which is 2.238%
