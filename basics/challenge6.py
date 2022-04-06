# breaking repeating-key xor
import base64
import math
from itertools import cycle


def get_plaintext_single_char(ciphertext, key):
    result = bytearray()
    for b in ciphertext:
        result.append(b ^ key)
    return bytes(result)


def get_plaintext(ciphertext, key):
    result = bytearray()
    for b, k in zip(ciphertext, cycle(key)):
        result.append(b ^ k)
    return bytes(result)


def score_plaintext(text):
    result = 0
    frequent_letters = b'etaoin shrdlu'
    for c in text:
        if c in frequent_letters:
            result += 1
    return result


# 0. Open and decode file
with open('data6.txt') as file:
    data = base64.b64decode(file.read())

# 1. Keysize
KEYSIZES = range(2, 40)


# 2. Hamming distance
def hamming_distance(buffer1, buffer2):
    distance = 0
    for byte1, byte2 in zip(buffer1, buffer2):
        distance += sum(bit1 != bit2 for bit1, bit2 in zip(f'{byte1:08b}', f'{byte2:08b}'))
    return distance


# 3. Find edit distances for each keysize
distances = {}
for keysize in KEYSIZES:
    distances[keysize] = (hamming_distance(data[:keysize], data[keysize:keysize + keysize]) + hamming_distance(
        data[keysize * 2:keysize * 3], data[keysize * 3:keysize * 4])) / keysize

# 4. Get possible key sizes
min_distances = {k: v for k, v in sorted(distances.items(), key=lambda x: x[1])}
possible_key_sizes = list(min_distances.keys())[:10]

# 5. For each keysize,
max_key_score = 0
best_key = None
for key_size in possible_key_sizes:

    # 5. break the ciphertext into blocks of keysize length.
    chunks_num = math.floor(len(data) / key_size)
    data_chunks = [data[key_size * c:key_size * (c + 1)] for c in range(chunks_num)]

    # 6. Now transpose the blocks
    transposed_data_chunks = []
    for byte in range(key_size):
        transposed_data_chunk = bytearray()
        for chunk in data_chunks:
            transposed_data_chunk.append(chunk[byte])
        transposed_data_chunks.append(bytes(transposed_data_chunk))

    # 7. Solve each block as if it was single char XOR
    # 8. Put best looking bytes together and you have the key
    max_bytes_keys = bytearray()
    for ciphertext in transposed_data_chunks:
        scores = {}
        for key in bytearray(range(255)):
            scores[key] = score_plaintext(get_plaintext_single_char(ciphertext, key))

        max_bytes_keys.append(max(scores, key=scores.get))

    # Score 'plaintext' for given multibyte key
    key_score = score_plaintext(get_plaintext(data, max_bytes_keys))
    if key_score > max_key_score:
        max_key_score = key_score
        best_key = max_bytes_keys

print('plaintext: ' + str(get_plaintext(data, best_key), 'utf-8'))
