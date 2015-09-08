from PIL import Image
import sys
import os.path
import files as files

def capacidad(filename):
	if files.file_exists(filename):
		image = Image.open(filename)
		xs, ys = image.size
		return xs * ys
	else:
		return None

#run in the 'package' directory
if __name__ == '__main__':
	print None
