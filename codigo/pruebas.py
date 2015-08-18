from PIL import Image, ImageDraw

#http://natureofcode.com/book/chapter-8-fractals/

def __main__():
	print "miau"
	filename = 'imagen.png'
	image = Image.open(filename)
	x, y = image.size
	x2, y2 = x / 2, y / 2
	pixels = image.load()
	print x, y, x2, y2
	if x > y:
		radio = y
	else:
		radio = x
	print radio
	pixels[x2, y2] = (255, 255, 255)
	image.show()
	return None
	
def drawCircle():
	return None
	
#Pasar a otro archivo
	
def getYCoordinate(y, ys):
	new_y = float((ys/2.0) - y)
	return new_y

def getXCoordinate(x, xs):
	new_x = float(x - (xs/2.0))
	return new_x
	
def getYPixel(y, ys):
	new_y = int((ys/2.0) - y)
	return new_y

def getXPixel(x, xs):
	new_x = int(x + (xs/2.0))
	return new_x

if __name__ == '__main__':
	__main__()