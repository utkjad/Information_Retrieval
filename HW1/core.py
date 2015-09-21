"""
Crawling starts here
"""

import requests
from bs4 import BeautifulSoup
import urllib2, urlparse 

def is_url_valid(master_page, href_text):
	"""
	"""
	return ":" not in href_text \
	and "http://en.wikipedia.org/wiki/" in urlparse.urljoin(master_page, href_text)\
	and "http://en.wikipedia.org/wiki/Main_Page" not in urlparse.urljoin(master_page, href_text)

def is_unique_url():

def crawl_main():#seed_page = "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher", keyphrase = ""):
	"""
	"""
	seed_page = "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher"
	response_obj = requests.get(seed_page)
	soup = BeautifulSoup(response_obj.content, "html.parser")

	unique_urls = []

	for link in soup.find_all('a', href = True):
		if is_url_valid(seed_page, link['href']):
			if is_unique_url(urlparse.urljoin(seed_page, link['href']), unique_urls):
			unique_urls.append(urlparse.urljoin(seed_page, link['href']))



	print unique_urls
	




crawl_main() #"http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher","")
