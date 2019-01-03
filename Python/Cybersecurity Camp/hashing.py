from Crypto.Hash import MD5, SHA, SHA256, SHA512

password = input("Enter password: ")

md5 = MD5.new()
md5.update(password.encode())

print("MD5 hash: {}".format(md5.hexdigest()))

sha = SHA.new()
sha.update(password.encode())

print("SHA hash: {}".format(sha.hexdigest()))

