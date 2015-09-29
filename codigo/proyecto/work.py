import hash_md5
import os
import primes
from PIL import Image

def generar_diccionario():
	dicc = {}
	valor = 16
	for dummy in xrange(0, 8):
		bits = "{0:03b}".format(dummy)
		dicc[valor] = bits
		valor *= 2
	return dicc

def start(md5_filename, mod_):
	aux = 1
	for c in md5_filename:
		aux = (aux * ord(c)) % mod_
	return aux

#original code from here http://stackoverflow.com/a/2104107
def length_file(filename):
	#checar si archivo existe
	statinfo = os.stat(filename)
	return statinfo.st_size

def find_bits_to_need(length):
	dicc_bits = generar_diccionario()
	length_bits = len(("{0:0b}").format(length))
	aux_bits_template = "{0:0b}".format(length_bits)
	aux_bits_list = ["1"] * len(aux_bits_template)
	aux_bits = "".join(aux_bits_list)
	aux_number = int(aux_bits, 2) + 1
	return (dicc_bits[aux_number], aux_number) #validar si es valido

def work(first_filename, second_filename):
	md5_filename = hash_md5.generate_file_md5(second_filename)
	length = length_file(first_filename) #del primer archivo
	start_ = start(md5_filename, length)
	print "MD5: {}, Longitud del primer archivo {}, inicio del algoritmo {}".format(md5_filename, length, start_)
	#image_.save(first_filename)
	prime = primes.find_prime(length)
	print prime, length
	bits_to_need_prime = find_bits_to_need(prime)
	print bits_to_need_prime

#en start_, si es una imagen entonces los tres bits de un pixel representan una longitud de bits
#si es un audio entonces lee tres bytes

filename = "CURP.png"
second = "RFC.png"
work(filename, second)
