# Data Structures  and there mutability

# Imutable ❌
# Number, Boolean, String, Tuple, Bytes, Frozen Sets

x = "Hello"
# x[0]="J"
# TypeError: 'str' object does not support item assignment

assert x[0] == "H"


tup = (1, 2, 3)


# Mutable ✅
# List, Set, Dict, Byte Arrays

arr = [1, 2, 3, 4, 5]
arr[0] = 10
assert arr[0] == 10


# Tuple is interesting
tup = ("hello", [1,2,3] )

tup[1][0] = 10  # ✅

assert tup[1][0] == 10


# ✅ Type Hinting
def add_numbers(a: int, b: int) -> int:
    return a + b
# Type hinting is not enforced at runtime, but it helps with code readability and IDE support.


# ✅ Comprehensions

squares = [x*x for x in range(5)]
assert squares == [0, 1, 4, 9, 16]



# ✅ Functions & Lambdas

def square(x):
    return x**2

assert square(5) == 25

# Lambda function
lambda x: x**2

assert (lambda x: x**2)(5) == 25

# ✅ Classes & @dataclass

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
assert p.x == 1
assert p.y == 2

# ✅ Generators
def generate_numbers(n):
    for i in range(n):
        yield i
gen = generate_numbers(5)

assert next(gen) == 0

# ✅ Decorators

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

# ✅ Chaining Context Managers
try:
    with open("file1.txt") as f1, open("file2.txt") as f2:
        data = f1.read() + f2.read()
except FileNotFoundError:
    print("Not Found")

# ✅ Asyncio (More in depth video on async will be part of this playlist)

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    
asyncio.run(main())