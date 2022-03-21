# convert hex to base64
import base64

some_bytes = bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
result = base64.b64encode(some_bytes)
print(result)