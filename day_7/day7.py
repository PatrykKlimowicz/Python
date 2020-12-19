# in Python You can put else block after a loop:
for i in range(3):
    print('Loop', i)
else:
    print('Else block!')  # runs immediately after the loop finishes

# ELSE in loops means "Do this when loop finished peacefully". So, break statement prevent else to execute
for i in range(3):
    print('Loop', i)
    if i == 2:
        break
else:
    print('Else block!')  # this won't be printed

# if you run over a empty sequence else is executed without problems
x = []
for i in x:
    print("Hello from for loop")
else:
    print("Hello from for-else!")

# if your loop never start else is there for You...
while False:
    print("Hello from while loop")
else:
    print("Hello from while-else!")

# there are of course some cases that else block after loop may seem useful
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print('Testing:', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime!')

# The above code works, however it is hard to understand for people that do not write it. It is not intuitive and not Pythonic. It's better to write a helper function for this. Simple constructs like loops should be self-evident in Python. You should avoid using else blocks after loops entirely.