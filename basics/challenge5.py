# implement repeating-key xor
from itertools import cycle

msg = b"Burning 'em, if you ain't quick and nimble \
I go crazy when I hear a cymbal"

key = b"ICE"


def encrypt(msg, key):
    result = bytearray()
    for b, k in zip(msg, cycle(key)):
        result.append(b ^ k)
    return bytes(result).hex()


print(encrypt(msg, key))