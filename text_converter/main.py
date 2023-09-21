import base64
import binascii

def b64(text: str):
	return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def b32(text: str):
	return base64.b32encode(text.encode('utf-8')).decode('utf-8')

def b16(text: str):
	return base64.b16encode(text.encode('utf-8')).decode('utf-8')

def b2(text: str):
	output = []
	for character in text:
	 	output.append(bin(ord(character))[2:].zfill(8))
	return " ".join(output)
	 
def a85(text: str):
	return base64.a85encode(text.encode('utf-8')).decode('utf-8')	 
	 

def to_hex(text: str):
	return binascii.hexlify(text.encode("utf-8")).decode("utf-8")

def ascii_pos(text: str):
	output = []
	for character in text:
	 	output.append(str(ord(character)))
	return " ".join(output) 
	
def main():
	while True:
		inpt = input("Enter String: ")
		if inpt == "exit":
			exit()
		print(f"Base 2: {b2(inpt)}")
		print(f"Base 16: {b16(inpt)}")
		print(f"Base 32: {b32(inpt)}")
		print(f"Base 64: {b64(inpt)}")
		print(f"Hexadecimal: {to_hex(inpt)}")
		print(f"Ascii 85: {a85(inpt)}")
		print(f"Ascii positions: {ascii_pos(inpt)}")
		
	
if __name__ == "__main__":
	main()
