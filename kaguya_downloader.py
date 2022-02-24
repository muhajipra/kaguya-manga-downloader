import os
import requests
import zipfile

# Initialize the Base Path to store the downloaded file
# Note: Will change to Input in later date
DOWNLOAD_DESTINATION = "D:/Ebook/Manga/Kaguya-sama"
DOWNLOAD_URL = "https://baka.guya.moe/api/download_chapter/Kaguya-Wants-To-Be-Confessed-To/"

# Create the directory
if os.path.isdir(DOWNLOAD_DESTINATION) is not True: # Check if the directory available
	os.mkdir(DOWNLOAD_DESTINATION)

# Initialize the start and end of the chapter to be downloaded
chapter_start = 1
chapter_end = 4

# Making function to download the manga
def download_manga(download_destination=DOWNLOAD_DESTINATION, download_url=DOWNLOAD_URL,
		chapter_start=chapter_start, chapter_end=chapter_end):
	for i in range(chapter_start, chapter_end+1):
		# Download the chapter
		chapter_url = download_url + str(i)
		request = requests.get(chapter_url)
		filename = "chapter {}.zip".format(i)
		file_path = os.path.join(download_destination, filename)
		# Store the file to download destination
		with open(file_path, "wb") as chapter:
			chapter.write(request.content)

		# Announce that the chapter is successfully downloaded
		print("Chapter {} has been downloaded".format(i))

download_manga(DOWNLOAD_DESTINATION,DOWNLOAD_URL, chapter_start, chapter_end)




