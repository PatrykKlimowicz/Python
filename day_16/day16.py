from collections import defaultdict  # needed from line 40


# There are situations when both setdefault and defaultdict (please look at previous days) methods are not the right fit. For example, we want to map picture name to its path in a normal dict instance and using get method to check for keys:
pictures = {}
path = 'picture_1234.jpeg'

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'failed to open path {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()
# When a file handle already exist in the dictionary, this code makes only a single dictionary access. In the case that file handle doesn't exist the dictionary is accessed once by get, and then it is assigned in the else clause. With setdefault this code will be:
try:
    handle = pictures.setdefault(path, open(path, 'a+b'))
except OSError:
    print(f'failed to open path {path}')
    raise
else:
    handle.seek(0)
    image_data = handle.read()


# This code has many problems. The open function to create the file handle is always called, even when the path is alreadt present in the dictionary. This results in an additional file handle that may conflict with existing one that is open in the same program. The open exception may be hard to differentiate from exceptions raised by setdefault method. If we'll be trying to manage the internal state the defaultdict might seem like the right choice:
def open_picture(path):
    try:
        return open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
        raise


try:
    pictures = defaultdict(open_picture)
    handle = pictures[path]
    handle.seek(0)
    image_data = handle.read()
except TypeError:
    print('defaultdict function should be parameterless!')
# The defaultdict expects function that do not require arguments. Fortunately, this situation is common enough that Python has another built-in solution. You can subclass the dict type and implement the __missing__ special method to add custom logic for handling missing keys. Here, I do this by defining a new class that takes advantage of the same open_picture helper method.


class Picture(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


path = 'picture_1235.jpeg'
pictures = Picture()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
# when the picture[path] dictionary access finds that the path key isn't present in the dictionary, the __missing__ method is called. This method must create the new default value for the key, insert it into the dictionary, and return it to the caller. If the key exist the __missing__ method is not called.
