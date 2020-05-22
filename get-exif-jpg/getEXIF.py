from PIL import Image
from PIL.ExifTags import TAGS
import PIL.Image as pillow

##############################################
#           #                   #            #
#            #                 #             #
############### By petitcroco ################
#            #                 #             #
#           #                   #            #
##############################################

print(pillow)
#.jpg

def exif(file):
	myExif = pillow.open(file)._getexif()
	for key, value in myExif.items():
		try:
		    key = int(key)
		    print('(UNKNOW by PIL) code=', key,' : ',value)
		except ValueError:
			print(key,' : ',value)

		name = TAGS.get(key, key)
		myExif[name] = myExif.pop(key)

	return myExif

exif('verre.jpg')
