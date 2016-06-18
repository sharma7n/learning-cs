# practice with generators

def natural_numbers(filter = lambda n: True):
    n = 0
    while True:
        n += 1
        if filter(n):
            yield n

for n in natural_numbers(lambda n: n % 3 == 0):
    if n > 100:
        break
    print(n)

def name_buffer():
    yield "Alice"
    yield "Bob"

for name in name_buffer():
    print(name)

import random
def random_numbers():
    while True:
        yield random.randint()

class SomeClass():

    _internal = []

    def iterate_through_list(self):
        for item in self._internal:
            yield item