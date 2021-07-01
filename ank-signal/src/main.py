import nacl.encoding
import nacl.hash

HASHER = nacl.hash.sha256
# could be nacl.hash.sha512 or nacl.hash.blake2b instead

# define a 1024 bytes log message
msg = 16*b'256 BytesMessage'
digest = HASHER(msg, encoder=nacl.encoding.HexEncoder)

# now send msg and digest to the user
print(nacl.encoding.HexEncoder.encode(msg))
print(digest)

