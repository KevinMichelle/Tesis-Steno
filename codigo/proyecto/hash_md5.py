import hashlib

#original code from this answer in Stack Overflow
#http://stackoverflow.com/a/1131255
def generate_file_md5(filename, blocksize=2**20):
	m = hashlib.md5()
	with open(filename , "rb") as f:
		while True:
  			buf = f.read(blocksize)
			if not buf:
				break
			m.update(buf)
	return m.digest()
