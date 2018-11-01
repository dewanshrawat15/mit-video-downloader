from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin
import urllib

def download_video(video_rel_url, name):
	download = urllib.request.FancyURLopener()
	download.retrieve(video_rel_url, name+".mp4")
	print(""+name+" downloaded")

def download_page(url, name):
	page = urlopen(url)
	parsed_page = BeautifulSoup(page, 'html.parser')
	req_link = parsed_page.find("a", text='Internet Archive').get("href")
	download_video(req_link, name)

def scrape_links(sc_link):
	src = urlopen(sc_link)
	codebase = BeautifulSoup(src, 'html.parser')
	url_list = codebase.findAll("a", attrs={"class": "medialink"})
	for i in url_list:
		name = i.getText()
		extracted_url = i.get("href")
		exact_url = urljoin(sc_link, extracted_url)
		download_page(exact_url, name)

def verify(pr_link):
	base = "https://ocw.mit.edu"
	if base in pr_link:
		scrape_links(pr_link)
	else:
		print("The following url is not a MIT-OCW link")

def main():
	link = input("Enter Download URL: ")
	verify(link)

main()