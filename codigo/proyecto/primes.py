import miller

def find_prime(possible_prime):
	prime_is_not_found = True
	if (possible_prime % 2 == 0):
		possible_prime += 1
	while (prime_is_not_found):
		is_prime = miller.miller(possible_prime)
		if (is_prime):
			prime_number = possible_prime
			prime_is_not_found = False
		possible_prime += 2
	return prime_number
