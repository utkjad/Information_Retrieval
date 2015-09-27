""" 
HW1 
Implmenting a simple focused web crawler for Wikipedia
"""
__author__ = "Utkarsh J"

import requests
from bs4 import BeautifulSoup
import urllib2
import urlparse
import time
import re 

# Keeps track of visited urls 
visited_urls = []
# URL frontier
url_frontier = []
# URL containing keyphrase, can have maximum 1000 such URLs.
urls_containing_keyphrase = []

def is_url_valid(current_page_url, href_text):
	""" Checks if url is in Wikipedia, not redirected to Main_Page and is an english page

	Arguments:
		current_page_url - URL of current page_url
		href_text -  text in anchor href tag

	Returns:
		True if URL is valid
	"""
	return ":" not in href_text \
		and "http://en.wikipedia.org/wiki/" in urlparse.urljoin(current_page_url, href_text)\
		and "http://en.wikipedia.org/wiki/Main_Page" not in urlparse.urljoin(current_page_url, href_text)

def is_unique_url(url):
	""" Checks if url is unique or not

	Arguments:
		url - current URL

	Returns:
		True if URL is unique
	"""
	return url not in [i[0] for i in visited_urls]

def real_crawling(keyphrase=None, maxdepth=5): 
	""" Function implementing crawling with or without keyphrase

	Arguements:
		keyphrase - word to be searched  
		maxdepth - total depth for crawling
	"""
	# Initialize depth and total crawled URLs.
	depth = 1 
	total_crawled_urls = 1
	track_depth = 0
	total_keyphrase_url = 1

	def _should_get_logged():
		if keyphrase == None:
			return len(url_frontier) != 0 and depth <= maxdepth and total_crawled_urls <= 1000
		else:
			return len(url_frontier) != 0 and depth <= maxdepth and total_keyphrase_url <= 1000

	# Apply BFS
	while _should_get_logged(): 
		page_url, depth =  url_frontier.pop(0)
		if is_unique_url(page_url):
			# print "CRAWLED=%d depth=%d FOR %s" %(total_crawled_urls, depth, page_url)
			# mark it visited
			visited_urls.append((page_url, depth))
			time.sleep(1)
			response_obj = requests.get(page_url)
			soup = BeautifulSoup(response_obj.content, "html.parser")
			total_crawled_urls = total_crawled_urls + 1

			def _get_children():
    				for link in soup.find_all('a', href=True):
						if is_url_valid(page_url, link['href']):
							whole_url = urlparse.urljoin(page_url, link['href'])
							# remove part after # if any
							if "#" in whole_url:
								whole_url = whole_url[:whole_url.find("#")]
							if is_unique_url(whole_url):
								url_frontier.append((whole_url, depth + 1))
			if keyphrase == None:
				_get_children()
			else:
				regex_keyphrase = re.compile(keyphrase, re.IGNORECASE)
				# remove scripts and footer
				for tag in soup.findAll(['script', 'form']) + soup.findAll(id="footer"):
					tag.extract()
				text = soup.get_text()
				lines = (line.strip() for line in text.splitlines())
				chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
				text = '\n'.join(chunk for chunk in chunks if chunk)
				if regex_keyphrase.search(text):
					urls_containing_keyphrase.append(page_url)
					total_keyphrase_url = total_keyphrase_url + 1
					# print "*%d)* CRAWLED=%d depth=%d FOR %s" %(total_keyphrase_url, total_crawled_urls, depth, page_url)
					# get unique children links
					_get_children()
			
def crawl(seed_page = unicode("http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher","utf-8"), keyphrase = None):
	""" Main entry crawl function
	Arguments:
		seed_page - the seed page, start page for crawling
		keyphrase - word to search in documents

	Returns:
		List of either visited URLs or list of URLs containing the keyphrase
	"""
	url_frontier.append((seed_page,1))
	
	if keyphrase == None:
		real_crawling(maxdepth = 5)
		return visited_urls
	else:
		real_crawling(keyphrase = keyphrase, maxdepth =5)
		return urls_containing_keyphrase


print "***********************"
print "1. URLs crawled upto depth 5 with limit of 1000 URLs"
start_time = time.time()
list_without_keyphrase = crawl()
end_time = time.time()
for i in list_without_keyphrase:
	print i[0]
print "TOTAL TIME %d" %(end_time - start_time)

# Keeps track of visited urls 
visited_urls = []
# URL frontier
url_frontier = []
# URL containing keyphrase, can have maximum 1000 such URLs.
urls_containing_keyphrase = []

print "***********************"
print "2. Unique URLs containing keyphrase"
start_time =  time.time()
list_with_keyphrase = crawl(keyphrase = "concordance")
end_time = time.time()
for i in list_with_keyphrase:
	print i
print "***************************"
print "TOTAL TIME %d" %(end_time - start_time)
