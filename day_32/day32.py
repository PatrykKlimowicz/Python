# yield expressions provide generator functions with a simple way to produce an iterable series of output values. It might seem that this is not bidirectional data stream, but it is. Let's create a program that will transmit radio signals:

import math


def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


# We can now transmit wave signal at single specified amplitude by iterating over the wave generator
def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')


def run(it):
    for output in it:
        transmit(output)


run(wave(3.0, 8))

# This works fine for producing basic waveforms, but it can’t be used to constantly vary the amplitude of the wave. We need a way to modulate the amplitude on each iteration of the generator. Python generators support the send method, which upgrades yield expressions into a two-way channel. The send method can be used to provide streaming inputs to a generator at the same time it’s yielding outputs.


# Presenting the idea:
def my_generator():
    received = yield 1
    print(f'received = {received}')


it = iter(my_generator())
output = next(it)  # Get first generator output
print(f'output = {output}')
try:
    next(it)  # Run generator until it exits
except StopIteration:
    pass


# With send:
it = iter(my_generator())
output = it.send(None)  # Get first generator output
print(f'output = {output}')
try:
    it.send('hello!')  # Send value into the generator
except StopIteration:
    pass


# We can use above behavior to manipulate amplitude in each iterator call
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield  # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output  # Receive next amplitude


def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))


# This works; it properly varies the output amplitude based on the input signal. The first output is None, as expected, because a value for the amplitude wasn’t received by the generator until after the initial yield expression. One problem with this code is that it’s difficult for new readers to understand: Using yield on the right side of an assignment statement isn’t intuitive, and it’s hard to see the connection between yield and send without already knowing the details of this advanced generator feature. Now, Instead of using a simple sine wave as my carrier, we need to use a complex waveform consisting of multiple signals in sequence:
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)


print('='*5, 'Mix of Simple Waves', '='*5)
run(complex_wave())  # OK


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)


print('='*5, 'Mix of Modulating Waves', '='*5)
run_modulating(complex_wave_modulating())  # NOT OK!

# This works to some extent, but the result contains a big surprise: There are many None values in the output! Why does this happen? When each yield next one. Each nested generator starts with a bare yield expression—one without a value—in order to receive the initial amplitude from a generator send method call. This causes the parent generator to output a None value when it transitions between child generators. Although it’s possible to work around this None problem by increasing the complexity of the run_modulating function, it’s not worth the trouble. It’s already difficult for new readers of the code to understand how send works. This surprising gotcha with yield from makes it even worse. My advice is to avoid the send method entirely and go with a simpler approach. The easiest solution is to pass an iterator into the wave function. The iterator should return an input amplitude each time the next built-in function is called on it. This arrangement ensures that each generator is progressed in a cascade as inputs and outputs are processed.


def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)  # Get next input
        output = amplitude * fraction
        yield output


# I can pass the same iterator into each of the generator functions that I’m trying to compose together. Iterators are stateful and thus each of the nested generators picks up where the previous generator left off.
def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)


run_cascading()
# The best part about this approach is that the iterator can come from anywhere and could be completely dynamic(e.g., implemented using a generator function). The only downside is that this code assumes that the input generator is completely thread safe, which may not be the case.
