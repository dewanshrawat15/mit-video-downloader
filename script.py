from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin
import urllib
import os.path
import requests
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system("clear")

def download_video(video_rel_url, name):
	filename = name + ".mp4"
	r = requests.get(video_rel_url, stream=True, timeout=10)
	file_size = int(r.headers['content-length'])
	if os.path.isfile(filename):
		file_size_local = os.stat(filename).st_size
		if file_size_local == file_size:
			print(""+filename+" => File already exists")
		else:
			print("Resuming download")
			file = open(filename)
			with open(filename, 'wb', int(file.seek(file_size_local))) as file:
				for chunk in r.iter_content(chunk_size=1024*1024):
						file.write(chunk)
	else:
		with open(filename, 'wb') as file:
			for chunk in r.iter_content(chunk_size=1024*1024):
				file.write(chunk)

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
	clear()
	link = input("Enter Download URL: ")
	verify(link)

main()