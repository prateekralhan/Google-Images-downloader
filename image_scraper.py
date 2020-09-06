import simple_image_download as simp

response = simp.simple_image_download

response().download(str(input("Enter the item: ")), int(input("Enter the number of images you wish to download: ")))