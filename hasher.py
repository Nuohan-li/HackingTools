import hashlib
from misc import *

# script used to encrypt a password -> used to test password cracker 

hash_algo = input("Enter a hashing algorith ")
string_to_hash = input("Enter a string to be hashed ")


if hash_algo == "md5":
    obj = hashlib.md5()
    obj.update(string_to_hash.encode())
    print(f"MD5: {obj.hexdigest()}")
elif hash_algo == "sha1":
    obj = hashlib.sha1()
    obj.update(string_to_hash.encode())
    print(f"SHA1: {obj.hexdigest()}")
elif hash_algo == "sha224":
    obj = hashlib.sha224()
    obj.update(string_to_hash.encode())
    print(f"SHA224: {obj.hexdigest()}")
elif hash_algo == "sha256":
    obj = hashlib.sha256()
    obj.update(string_to_hash.encode())
    print(f"SHA256: {obj.hexdigest()}")
elif hash_algo == "sha512":
    obj = hashlib.sha256()
    obj.update(string_to_hash.encode())
    print(f"SHA512: {obj.hexdigest()}")
else:
    log_error(f"Hashing algorithm {hash_algo} not supported")
