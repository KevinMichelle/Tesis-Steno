from PIL import Image
import sys
import os.path
import files as files
import itertools

def capacidad(filename):
	if files.file_exists(filename):
		image = Image.open(filename)
		xs, ys = image.size
		return xs * ys
	else:
		return None
		
def number_to_bits(number, bits):
	binary_string_auxiliar = "{0:0" + str(bits) + "b}"
	return binary_string_auxiliar.format(number)
	
def bits_to_number(bits):
	return int(bits, 2)
	
def get_list_of_bits(_string):
	list_of_numbers = []
	for character in _string:
		list_of_numbers.append(ord(character))
	list_of_bits_auxiliar = []
	for number in list_of_numbers:
		list_of_bits_auxiliar.append(number_to_bits(number, 8))
	return "".join(list_of_bits_auxiliar)
	
def replace_last_bit(bits, new_bit):
	return bits[0:len(bits) - 1] + new_bit
	
def image_steganography(filename, _string, is_text):
	if files.file_exists(filename):
		image = Image.open(filename)
		list_of_pixels = image.load()
		list_of_bits = get_list_of_bits(_string)
		print list_of_bits, len(list_of_bits)
		xs, ys = image.size
		total_bits = len(list_of_bits) + 8 #to fills zeroes
		if total_bits % 3 > 0:
			total_bits = total_bits + (3 - (total_bits % 3))
		bool_break = False
		hint_element = list_of_pixels[0, 0][0]
		hint_element_bits = number_to_bits(hint_element, 8)
		if is_text:
			new_bit = '1'
		else:
			new_bit = '0'
		counter = 1
		new_hint_element_bits = replace_last_bit(hint_element_bits, new_bit)
		print "total", total_bits
		image.show()
		for y, x in itertools.product(xrange(ys), xrange(1, xs)):
			actual_pixel = list_of_pixels[x, y]
			new_pixel = []
			for element in actual_pixel:
				element_bits = number_to_bits(element, 8)
				if counter > len(list_of_bits):
					new_bit = '0'
				else:
					new_bit = list_of_bits[counter - 1]
				new_element_bits = replace_last_bit(element_bits, new_bit)
				new_element = bits_to_number(new_element_bits)
				new_pixel.append(new_element)
				if counter >= total_bits:
					bool_break = True
					break
				counter += 1
			list_of_pixels[x, y] = tuple(new_pixel)
			if bool_break:
				break
		image.show()
		return None
		

#run in the 'package' directory
if __name__ == '__main__':
	image_steganography('captura1.png', 'Hola.', True)