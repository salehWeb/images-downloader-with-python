from PIL import Image
import requests

print("Enter a url to download: ")
url = input()
print("Enter a name for an image: ")
Image_name = input()
print("Downloading image...")


try:
	response = requests.get(url)
	if response.status_code == 200:
		with open(Image_name + ".png", 'wb') as f:
			f.write(response.content)
			f.close()
			print("Image downloaded successfully")
			print("Image saved as " + Image_name)
			img = Image.open(Image_name + '.png')
			img.show()		
except:
  print("Error downloading image")

exit()
