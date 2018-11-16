# MIT Video Downloader
The ```script.py``` file once triggered automatically starts downloading the videos from the course page which contains those lecture videos. The code supports reusability. Just import the ```Downloader``` object in your script from the mitocwdl.py file.

# Requirement
Any system with python 3 (preferably 3.6) and terminal.

# Usage
If you have to just download videos or basically use the script to download videos:
- Navigate to the file directory where the downloaded file (the script file) is stored using the cd command in terminal or cmd.
- Trigger ```python script.py``` or ```python3 script.py``` according to the operating system needs.
- Enter the url of the Video Lecture Course that you want to download.

If you want to use the Downloader object in other scripts:
- Copy paste the mitocwdl.py file wherever you are gonna write your script
- In your script, use ```from mitocwdl import Downloader``` to import the ```Downloader``` object
- Call the ```Downloader.verify()``` method to start downloading lecture videos

# Known Issue
None as of now. Currently, I'm trying to add a Resume Downloads Feature. Feel free to open an issue if any!

# License
> The MIT License