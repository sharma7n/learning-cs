#!/usr/bin/python
# -*- coding: utf-8 -*-
# closures practice

# argument is a variable


def adder(const):
    """ The interior function add_func is bound to the passed in const."""

    def add_func(param):
        return param + const

    return add_func


# argument is a function

def repeat(func):
    """ Executes a function twice. """

    def do_twice():
        func()
        func()

    return do_twice


# argument is a class

def extract_method(cls, method_name):
    """ Creates a function that represents a class method but is bound to a newly-created instance. """

    my_instance = cls('')

    def extracted_method(*args):
        method_name(my_instance, *args)

    return extracted_method


if __name__ == '__main__':

    # test adder

    add_5 = adder(5)
    add_7 = adder(7)
    assert add_5(3) == 8
    assert add_7(3) == 10


            # syntactic sugar for: say_hello = repeat(say_hello)

    @repeat
    def say_hello():
        print('hello!')

    say_hello() # >> hello! hello!


    class Dog:

        def __init__(self, name):
            self.name = name

        def bark(self):
            print(self.name + ' bark!')


    dogs = [Dog(s) for s in ['Muffin', 'Gumshoe', 'Toodles']]
    for dog in dogs:
        dog.bark() # >> Muffin bark! Gumshoe bark! Toodles bark!

    generic_bark = extract_method(Dog, Dog.bark)
    generic_bark() # >> bark!


    def new_bark(self):
        print(self.name + ' woof!')


    Dog.bark = new_bark

    for dog in dogs:
        dog.bark() # >> Muffin woof! Gumshoe woof! Toodles woof!

    generic_bark() # >> bark!
