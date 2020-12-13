from locale import getpreferredencoding  # needed for open exapmle

# bytes simple example
b = b'h\x65llo'
print(list(b))  # [104, 101, 108, 108, 111]
print(b)  # b'hello'

# str simple example
s = 'a\u0300 propos'
print(list(s))  #
print(s)  #

# str to bytes ==> use encode
# bytes to str ==> use decode
# The split between character types leads to two common situations
# in Python code:
# - You want to operate on bytes sequences that contains UTF-8 encoded str
# - You want to operate on Unicode strings
# These two situations are possible with following helper function:


def to_str(bytes_or_string):
    if isinstance(bytes_or_string, bytes):
        value = bytes_or_string.decode('utf-8')
    else:
        value = bytes_or_string

    return value  # instance of str


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


def to_bytes(bytes_or_string):
    if isinstance(bytes_or_string, str):
        value = bytes_or_string.encode('utf-8')
    else:
        value = bytes_or_string

    return value  # instance of bytes


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


# to make operations You cannot mix str and bytes!
# in case of reading and writing from/to a file use 'rb' and 'wb' flags

with open("data.bin", 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

with open("data.bin", 'rb') as f:
    data = f.read()

assert data == b'\xf1\xf2\xf3\xf4\xf5'  # True, no exception

# to be 100% safe use encoding parameter of open. It's value can be checked:
print(getpreferredencoding())
