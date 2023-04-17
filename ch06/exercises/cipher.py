import string
from cryptography import fernet

message = "The quick brown fox jumps over the lazy dog"

shift = 3

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
caesar = str.maketrans(alphabet, shifted)

encrypted = message.translate(caesar)

with open("encrypted.txt", "a") as f:
  print(encrypted)
