from time import sleep
from datetime import datetime
import json
from typing import Optional


# Sometimes we need a dynamic value as a default for keyword argument
def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hi there!')
sleep(1)
log('Hi there, but 1 sec later!')  # accually the time is the same!


# The timestamps are the same because datetime.now() is evaluated only once - when the function is defined. The default values are evaluated only once - when a program starts up so after run day22.py the datetime.now() won't be evaluated anymore! To fix this we need to assign a None as default value and document the bahavior in docstring:
def log_1(message, when=None):
    """Log a message with timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_1('Hi there!')
sleep(1)
log_1('Hi there, but 1 sec later!')  # now it's working as expected!


# Using None as default is expecially important when the arguments are mutable.
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# Problem here is same as in log function. Default parameter will be evaluated only once and share between function call.
foo = decode('bad data')
foo['staff'] = 5
bar = decode('again bad data')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# We need two different dictionaries with a sigle key-value element but insted we have the same dictionary in foo and bar. The foo and bar are the same dict object:
assert foo is bar  # OK


def decode_1(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


# Now the code from before works as expected:
foo = decode_1('bad data')
foo['staff'] = 5
bar = decode_1('again bad data')
bar['meep'] = 1
print('Foo:', foo)  # staff: 5
print('Bar:', bar)  # meep: 1


# This approach also works with type annotations:
def log_typed(message: str, when: Optional[datetime] = None) -> None:
    """Log a message with timepstamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_typed('Hello')
sleep(1)
when = datetime.now()
sleep(1)
log_typed('World', when)
