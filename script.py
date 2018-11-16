from os import system, name
from mitocwdl import Downloader

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system("clear")

clear()
link = input("Enter Download URL: ")
download = Downloader()
download.verify(link)