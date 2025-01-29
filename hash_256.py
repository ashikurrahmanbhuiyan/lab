import hashlib
string = "Hello, world!"
hash_object = hashlib.sha256()
hash_object.update(string.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print("String: {}".format(string))
print("Hash value (SHA-256): {}".format(hex_dig))