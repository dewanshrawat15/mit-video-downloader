from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin
import urllib
import os.path
import requests
import sys
from os import system, name

class Downloader(object):

	def progress(self, localsize, filesize):
		if localsize == 0:
			percent = 0
		else:
			percent = (localsize/filesize) * 100
			percent = int((round(percent, 2)))
		output = "\r %s%% downloaded" % percent
		sys.stdout.write(output)
		sys.stdout.flush()

	def download_video(self, video_rel_url, name):
		filename = name + ".mp4"
		r = requests.get(video_rel_url, stream=True)
		file_size = int(r.headers['content-length'])
		if os.path.isfile(filename):
			file_size_local = os.stat(filename).st_size
			if file_size_local == file_size:
				print(""+filename+" => File already exists")
			else:
				print("Reinitiating Download")
				with open(filename, 'wb') as file:
					for chunk in r.iter_content(chunk_size=1024*1024):
						file.write(chunk)
						file_size_local = os.stat(filename).st_size
						self.progress(file_size_local, file_size)
				print("\n"+filename+" downloaded")
		else:
			print("Downloading")
			with open(filename, 'wb') as file:
				for chunk in r.iter_content(chunk_size=1024*1024):
					file.write(chunk)
					file_size_local = os.stat(filename).st_size
					self.progress(file_size_local, file_size)
			print("\n"+filename+" downloaded")

	def download_page(self, url, name):
		page = urlopen(url)
		parsed_page = BeautifulSoup(page, 'html.parser')
		req_link = parsed_page.find("a", text='Internet Archive').get("href")
		self.download_video(req_link, name)

	def scrape_links(self, sc_link):
		src = urlopen(sc_link)
		codebase = BeautifulSoup(src, 'html.parser')
		url_list = codebase.findAll("a", attrs={"class": "medialink"})
		for i in url_list:
			name = i.getText()
			name = str(name)
			extracted_url = i.get("href")
			exact_url = urljoin(sc_link, extracted_url)
			self.download_page(exact_url, name)

	def verify(self, pr_link):
		base = "https://ocw.mit.edu"
		if base in pr_link:
			self.scrape_links(pr_link)
		else:
			print("The following url is not a MIT-OCW link")