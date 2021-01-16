# generators are so useful in programming and bring solution to common problems.Generators are so useful that many programs start to look like layers of generators strung together. Let's say we need to animate something on the screen:
def move(period, speed):
    for _ in range(period):
        yield speed


def pause(delay):
    for _ in range(delay):
        yield 0

# to create animation we need to combine this two generators together:


def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta


# to render animation on the screen:
def render(delta):
    print(f'Delta: {delta:.1f}')


def run(func):
    for delta in func():
        render(delta)


# We can now run animation
run(animate)


# The problem with this code is the repetitive nature of the animate function.The redundancy of the for statements and yield expressions for each generator adds noise and reduces readability. This example includes only three nested generators and it’s already hurting clarity. The solution to this problem is to use the yield from expression. This advanced generator feature allows you to yield all values from a nested generator before returning control to the parent generator
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(4, 3.0)


run(animate_composed)

# The result is the same as before, but now the code is clearer and more intuitive. yield from essentially causes the Python interpreter to handle the nested for loop and yield expression boilerplate for you, which results in better performance.
