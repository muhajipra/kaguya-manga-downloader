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
chapter_start = 60
chapter_end = 60

link_1 = ["60", "70", "80", "91", "101", "109", "111", "121", "131", "141", "151", "161", 
		"171", "172", "181", "191", "201", "211", "221", "231", "241"]
link_5 = ["5", "10", "20", "27", "30", "40", "45", "46", "50", "64", "83", "101"]

# Making function to download the manga
def download_manga(download_destination=DOWNLOAD_DESTINATION, download_url=DOWNLOAD_URL,
		chapter_start=chapter_start, chapter_end=chapter_end):
	'''This function is used to download chapter when given the destination to store the downloaded
	file, url to download from, the range of chapter to download'''
	for i in range(chapter_start, chapter_end+1):
		# Skip download if file already exist
		if os.path.isdir(download_destination + "/Chapter {}".format(i)):
			continue
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

		# Download the extra chapter
		if str(i) in link_1:
			extra_chapter = download_url + str(i) + "-1"
			filename = "chapter {}-1.zip".format(i)
		elif str(i) in link_5:
			extra_chapter = download_url + str(i) + "-5"
			filename = "chapter {}-5.zip".format(i)
		else:
			continue
		extra_request = requests.get(extra_chapter)
		file_path = os.path.join(download_destination, filename)
		# Store the file to download destination
		with open(file_path, "wb") as chapter:
			chapter.write(extra_request.content)

		if str(i) in link_1:
			print("Chapter {}-1 has been downloaded".format(i))
		elif str(i) in link_5:
			print("Chapter {}-5 has been downloaded".format(i))

def zip_extractor(download_destination=DOWNLOAD_DESTINATION):
	'''This function is used to extract every chapter in the directory and
	delete the zip file after it completes'''

	# Extract the file
	for i, chapter in enumerate(os.listdir(download_destination)):
		zip_path = os.path.join(download_destination, chapter)
		if os.path.isdir(zip_path):
			continue
		name = chapter[:-4]
		chapter_dir = os.path.join(download_destination, name)

		print("Unzipping {}".format(chapter))
		with zipfile.ZipFile(zip_path, "r") as zip_chapter:
			zip_chapter.extractall(chapter_dir)
		os.remove(zip_path)

download_manga(DOWNLOAD_DESTINATION,DOWNLOAD_URL, chapter_start, chapter_end)
zip_extractor(DOWNLOAD_DESTINATION)



