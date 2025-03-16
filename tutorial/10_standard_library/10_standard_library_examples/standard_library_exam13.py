


import zlib

s = b'witch which has which witches wrist watch'

print(len(s))
# 41

t = zlib.compress(s)

print(t)
# b'x\x9c+\xcf,I\xceP(\xcf\xc8\x04\x92\x19\x89\xc5PV9H4\x15\xc8+\xca,.Q(O\x04\xf2\x00D?\x0f\x89'

print(zlib.decompress(t))
# b'witch which has which witches wrist watch'

print(zlib.crc32(s))
# 226805979