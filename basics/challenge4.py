# detect single-character XOR
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
    with open('data4.txt', 'r') as data:
        for ciphertext in data:
            max_key_score = 0
            for key in bytearray(range(255)):
                plaintext = get_plaintext(bytes.fromhex(ciphertext), key)
                key_score = score_plaintext(plaintext)
                if key_score > max_key_score:
                    max_key_score = key_score
                    scores[plaintext] = max_key_score

    max_score_text = max(scores, key=scores.get)
    print('plaintext: ' + str(max_score_text, 'utf-8'))
