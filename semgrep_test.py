# cf. https://github.com/PyCQA/bandit/blob/b78c938c0bd03d201932570f5e054261e10c5750/examples/crypto-md5.py

from cryptography.hazmat.primitives import hashes

# ruleid:insecure-hash-algorithm-md5
hashes.SHA1()
# ruleid:insecure-hash-algorithm-sha1
hashes.SHA256()
# ok:insecure-hash-algorithm-sha1
# ok:insecure-hash-algorithm-md5
hashes.SHA256()
# ok:insecure-hash-algorithm-sha1
# ok:insecure-hash-algorithm-md5
hashes.SHA3_256()
digest = hashes.Hash(hashes.SHA256())
digest.update(b"abcdefg")
product = digest.finalize()
print(product.hex())
# echo -n "abcdefg" | md5
# 7ac66c0f148de9519b8bd264312c4d64
fileDigest = hashes.Hash(hashes.MD5())

with open("test.txt", 'rb') as reader:
    # Read and add line to fileDigest
    for line in reader:
        fileDigest.update(line)

fileProduct = fileDigest.finalize()
print(fileProduct.hex())
# 298b5f666156316f802ea35fb2ee887d
# md5 test.txt
# MD5 (test.txt) = 298b5f666156316f802ea35fb2ee887d
