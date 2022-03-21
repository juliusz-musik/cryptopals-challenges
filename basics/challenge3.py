# single-byte XOR cipher
ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
frequent_letters = b'etaoin shrdlu'


def get_plaintext(ciphertext, key):
    result = bytearray()
    for b in ciphertext:
        result.append(b ^ key)
    return bytes(result)


def score_plaintext(text):
    result = 0
    for c in text:
        if c in frequent_letters:
            result += 1
    return result


if __name__ == '__main__':
    scores = {}
    for key in bytearray(range(255)):
        scores[key] = score_plaintext(get_plaintext(ciphertext, key))

    max_key = max(scores, key=scores.get)
    print('plaintext: ' + str(get_plaintext(ciphertext, max_key), 'utf-8'))
    print('key: ' + hex(max_key))
