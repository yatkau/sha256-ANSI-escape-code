import hashlib


def stdin_hash():
    raw = input('Input: ')
    hex_s = raw.replace(r'\x', '')
    text = bytearray.fromhex(hex_s)
    hash_object = hashlib.sha256(text)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def main():
	while True:
		try:
			result = stdin_hash()
		except ValueError:
			print("Please input ANSI escape code, like \xF0\x9F\x98\x81")
		print(result)


if __name__ == '__main__':
	main()
