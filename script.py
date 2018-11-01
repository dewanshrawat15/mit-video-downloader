from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin

def download_page(url):
	page = urlopen(url)
	parsed_page = BeautifulSoup(page, 'html.parser')
	downloadlinks_list = parsed_page.findAll("a")
	print(downloadlinks_list)

def scrape_links(link):
	src = urlopen(link)
	codebase = BeautifulSoup(src, 'html.parser')
	url_list = codebase.findAll("a", attrs={"class": "medialink"})
	for i in url_list:
		extracted_url = i.get("href")
		exact_url = urljoin(link, extracted_url)
		download_page(exact_url)

def verify(link):
	base = "https://ocw.mit.edu"
	if base in link:
		scrape_links(link)
	else:
		print("The following url is not a MIT-OCW link")

def main():
	link = input("Enter Download URL: ")
	verify(link)

main()