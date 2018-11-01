from bs4 import BeautifulSoup
from urllib.request import urlopen

src = urlopen("https://dewanshrawat.me/lastofus/")
codebase = BeautifulSoup(src, 'html.parser')
print(codebase.title.string)