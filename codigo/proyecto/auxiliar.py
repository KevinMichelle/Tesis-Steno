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
		xs, ys = image.size
		total_bits = len(list_of_bits) + 8 #to fills zeroes
		if total_bits % 3 > 0:
			total_bits = total_bits + (3 - (total_bits % 3))
		bool_break = False
		hint_element = list_of_pixels[0, 0][0]
		hint_element_bits = number_to_bits(hint_element, 8)
		if is_text:
			hint_bit = '1'
		else:
			hint_bit = '0'
		counter = 1
		new_hint_element_bits = replace_last_bit(hint_element_bits, hint_bit)
		new_hint = bits_to_number(new_hint_element_bits)
		first_tuple = list_of_pixels[0, 0]
		new_tuple = (new_hint, first_tuple[1], first_tuple[2])
		list_of_pixels[0, 0] = new_tuple
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
		image.save(filename)
		return None
		
def check_bits(list_of_bits, sub_string_bits):
	string_ = "".join(list_of_bits)
	if sub_string_bits in string_:
		return True
	else:
		return False
		
def get_character(bits):
	return None
	
def loop_bits(bits):
	return None
		
def search_image_steganography(filename):
	if files.file_exists(filename):
		image = Image.open(filename)
		list_of_pixels = image.load()
		xs, ys = image.size
		bool_quit = False
		hint_element = list_of_pixels[0, 0][0]
		hint_element_bits = number_to_bits(hint_element, 8)
		hint_bit = hint_element_bits[len(hint_element_bits) - 1]
		is_text = False
		if hint_bit == '1':
			is_text = True
		list_of_bits = []
		need_to_break = False
		for y, x in itertools.product(xrange(ys), xrange(1, xs)):
			actual_pixel = list_of_pixels[x, y]
			for element in actual_pixel:
				element_bits = number_to_bits(element, 8)
				list_of_bits.append(element_bits[len(element_bits) - 1])
			if is_text:
				need_to_break = check_bits(list_of_bits, "00000000")
			if need_to_break:
				break
		string_bits = "".join(list_of_bits[0:len(list_of_bits)-9])
		total_characters = len(string_bits) / 8
		list_of_characters = []
		for n in xrange(1, total_characters + 1):
			last = (n * 8)
			first = last - 8
			sub_string_bits = string_bits[first:last]
			new_number = bits_to_number(sub_string_bits)
			list_of_characters.append(chr(new_number))
		return "".join(list_of_characters)

#run in the 'package' directory
if __name__ == '__main__':
	image_steganography('captura1.png', 'hola como estas este es un mensaje oculto nundfnudnfudnufdnfd .', True)
	print search_image_steganography('captura1.png')