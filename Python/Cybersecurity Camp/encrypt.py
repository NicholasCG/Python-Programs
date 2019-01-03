# goal: use a symmetric cipher (AES)

# requires: pip install pycrypto

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util import Counter

msg = input("Enter a message: ")
password = input("Enter a password: ")

sha256 = SHA256.new()
sha256.update(str.encode(password))
key_hash = sha256.digest()
key_hash_printable = sha256.hexdigest()
print("Hash of key: {}".format(key_hash_printable))

iv = Random.new().read(AES.block_size) # create random IV (initialization vector)
print("Randomly generated IV: {}".format(iv))
cipher = AES.new(key_hash, AES.MODE_CBC, iv)
# might need to pad the msg to a multiple of 16 characters
extra = len(msg) % 16
if extra > 0:
    msg = msg + (' ' * (16 - extra))
msg_enc = iv + cipher.encrypt(msg.encode()) # prepend IV so it's in the message
print("Encrypted: {}".format(msg_enc))

# ... save msg_enc, remember password ...

# extract IV (assuming we don't have the variable from earlier)
iv = msg_enc[0:16]
msg_enc = msg_enc[16:]
# recreate cipher object, won't work if we reuse prior
cipher2 = AES.new(key_hash, AES.MODE_CBC, iv)
msg_dec = cipher2.decrypt(msg_enc)
print("Decrypted: {}".format(msg_dec))
msg_dec_utf8 = msg_dec.decode('utf-8')
print("Decrypted: \"{}\"".format(msg_dec_utf8))
