import random
import pickle
import os.path
import getpass
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES



db = {}

def encrypt(data, password):
	sha256 = SHA256.new()
	sha256.update(str.encode(password))
	key_hash = sha256.digest()
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key_hash, AES.MODE_CBC, iv)
	extra = len(data) % 16
	if extra > 0:
		data = data + (b' ' * (16 - extra))
	data_enc = iv + cipher.encrypt(data)
	return data_enc

def decrypt(data_enc, password):
	sha256 = SHA256.new()
	sha256.update(str.encode(password))
	key_hash = sha256.digest()
	iv = data_enc[0:AES.block_size]
	data_enc = data_enc[AES.block_size:]
	cipher = AES.new(key_hash, AES.MODE_CBC, iv)
	data = cipher.decrypt(data_enc)
	return data

def save_passwords(password):
	with open("passwords.pkl", "wb") as f:
		data = pickle.dumps(db)
		data_enc = encrypt(data, password)
		f.write(data_enc)

def load_passwords(password):
	global db
	if os.path.exists("passwords.pkl"):
		with open("passwords.pkl", "rb") as f:
			data = decrypt(f.read(), password)
			db = pickle.loads(data)


def generate_password():
	length = random.randint(10,15)
	password = ""
	for i in range(length):
		password += chr(random.randint(33, 126))
	return password

key  = getpass.getpass("Password: ")

load_passwords(key)

while True:
	cmd = input("Type 'new' or 'show' or 'quit': ")

	if cmd == "new":
		website = input("Website: ")
		username = input("Username: ")
		password = generate_password()
		print("Generated password: {}".format(password))
		if website in db:
			db[website].append((username, password))
		else:
			db[website] = [(username, password)]
		save_passwords(key)
	elif cmd == "show":
		website = input("Website: ")
		if website in db:
			for (username, password) in db[website]:
				print("{} {}".format(username, password))
		else:
			print("Unknown website")

	elif cmd == "quit":
		break

