from bs4 import *
import requests
import os

# create storage space
def image_storage(images):
	try:
		folder = input("Enter Your Folder Name : ")
		os.mkdir(folder)

	except:
		print("Folder Already Exists")
		image_storage()

	download_images(images, folder)


#validation and download
def download_images(images, folder):
	count = 0
	print(f"Total {len(images)} Image Found!")

	if len(images) != 0:
		for i, image in enumerate(images):
	
			try:
				image_link = image["data-srcset"]

			except:

				try:
					image_link = image["data-src"]

				except:

					try:
						image_link = image["data-fallback-src"]

					except:

						try:
							image_link = image["src"]

						except:
							pass

			try:
				r = requests.get(image_link).content

				try:
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					with open(f"{folder}/images{i+1}.jpg", "wb+") as f:
						f.write(r)
					count += 1
                    
			except:
				pass

		if count == len(images):
			print("Download Complete")

		else:
			print(f"{count} Images Downloaded Out of {len(images)}")

#main function
def get_all_images(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	images = soup.findAll('img')
	image_storage(images)

#input url
url = input("Enter your URL address here: ")

get_all_images(url)