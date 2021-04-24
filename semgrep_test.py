from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


digest = hashes.Hash(hashes.SHA256())
digest.update(b"abcdefg")
product = digest.finalize()
print(product.hex())
# echo -n "abcdefg" | md5
# 7ac66c0f148de9519b8bd264312c4d64
fileDigest = hashes.Hash(hashes.SHA256())

with open("test.txt", 'rb') as reader:
    # Read and add line to fileDigest
    for line in reader:
        fileDigest.update(line)

fileProduct = fileDigest.finalize()
print(fileProduct.hex())
# 298b5f666156316f802ea35fb2ee887d
# md5 test.txt
# MD5 (test.txt) = 298b5f666156316f802ea35fb2ee887d
ec.generate_private_key(curve=ec.SECP256K1, backend=backends.default_backend())
# SECP256K1 Good
# SECP192R1 & SECT163K1 Bad
# ruleid: insufficient-ec-key-size
ec.generate_private_key(ec.SECP256K1, backends.default_backend())
fileDigest2 = hashes.Hash(hashes.MD5())
with open("test.txt", 'rb') as reader:
    # Read and add line to fileDigest
    for line in reader:
        fileDigest2.update(line)

fileProduct2 = fileDigest2.finalize()
print(fileProduct2.hex())

print("Test hash algorithm MD5 is weak")
print("Done")
fileDigest3 = hashes.Hash(hashes.MD5())
with open("test.txt", 'rb') as reader:
    # Read and add line to fileDigest
    for line in reader:
        fileDigest3.update(line)

fileProduct3 = fileDigest3.finalize()
print(fileProduct3.hex())