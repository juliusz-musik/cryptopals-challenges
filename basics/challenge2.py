# fixed XOR

def fixed_xor(buffer1, buffer2):
    result = bytearray()
    for b1,b2 in zip(buffer1, buffer2):
        result.append(b1 ^ b2)
    return bytes(result).hex()


print(fixed_xor(bytes.fromhex('1c0111001f010100061a024b53535009181c'),
      bytes.fromhex('686974207468652062756c6c277320657965')))
