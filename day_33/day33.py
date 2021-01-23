# generators support throw expressions that works in simple manner: When the method is called, the next occurrence of a yield expression re-raises the provided Exception instance after its output is received instead of continuing normally:

class MyError(Exception):
    pass


def my_generator():
    yield 1
    yield 2
    yield 3


it = my_generator()
print(next(it))  # Yield 1
print(next(it))  # Yield 2
# print(it.throw(MyError('test error')))  # uncomment this at first run
# When you call throw, the generator function may catch the injected exception with a standard try/except compound statement that surrounds the last yield expression that was executed


def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3
    yield 4


it = my_generator()
print(next(it))  # Yield 1
print(next(it))  # Yield 2
print(it.throw(MyError('test error')))

# This functionality provides a two-way communication channel between a generator and its caller that can be useful in certain situations. For example, imagine that we are trying to write a program with a timer that supports sporadic resets. Here, we'll implement this behavior by defining a generator that relies on the throw method:


class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


# In this code, whenever the Reset exception is raised by the yield expression, the counter resets itself to its original period. I can connect this counter reset event to an external input that’s polled every second. Then, I can define a run function to drive the timer generator, which injects exceptions with throw to cause resets, or calls announce for each generator output:
def check_for_reset():
    # Poll for external event
    a = int(input('Input 1 to reset timer or 0 to continue: '))
    return True if a else False


def announce(remaining):
    print(f'{remaining} ticks remaining')


def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)


run()


# This code works as expected, but it’s much harder to read than necessary. The various levels of nesting required to catch StopIteration exceptions or decide to throw, call next, or announce make the code noisy. A simpler approach to implementing this functionality is to define a stateful closure using an iterable container:
print("======== STATEFUL CLOSURE ==========\n\n")


class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)


run()
# The output matches the earlier version using throw, but this implementation is much easier to understand, especially for new readers of the code. Often, what you’re trying to accomplish by mixing generators and exceptions is better achieved with asynchronous features. Thus, it is suggested to avoid using throw entirely and instead use an iterable class if you need this type of exceptional behavior.
