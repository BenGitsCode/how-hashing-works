import hashlib as hash

sha = hash.sha256()

# insert the string we want to hash
sha.update('Hello World!')

# print the hexadecimal format of the binary hash we just created.
print sha.hexdigest()


# WARNING: Do NOT do this with large files.
# For large files, see the snippet here -> https://gist.github.com/aunyks/042c2798383f016939c40aa1be4f4aaf
with open('message.txt', 'txt') as test_file:
  file_buffer = test_file.read()
  sha.update(file_buffer)
  print sha.hexdigest()
