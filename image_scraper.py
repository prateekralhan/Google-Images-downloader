import simple_image_download as simp

response = simp.simple_image_download

#response().download(str(input("Enter the item: ")), int(input("Enter the number of images you wish to download: ")))
keywords_to_search = ['audi','mercedes','lamborghini']
no_of_images_to_download = 5000

for keyword in keywords_to_search:
	print("Downloading ",keyword," images...")
	response().download(keyword,no_of_images_to_download)
	print("-"*50)
