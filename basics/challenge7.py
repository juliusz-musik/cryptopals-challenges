import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

with open('data7.txt') as file:
    data = base64.b64decode(file.read())

key = b"YELLOW SUBMARINE"

cipher = Cipher(algorithms.AES(key), modes.ECB())
decryptor = cipher.decryptor()

print(decryptor.update(data))
