# How Python Works !!
# AST GIL Bytecode Memory and CPython

# Python first parses your code into an Abstract Syntax Tree (AST), 
# then compiles it into bytecode — 
# a set of low-level instructions that run on the Python Virtual Machine.



# AST: How python executes code

import ast

source = "a = 1 + 2"
parsed = ast.parse(source)
# print(ast.dump(parsed, indent=4))







# Python stores simple variables like x on the stack, 
# but objects like lists live on the heap. Lists are mutable, 
# so changes inside a function affect them outside too

def demo():
    x = 10         # Immutable
    y = [1, 2, 3]  # Mutable
    y.append(4)
    # print(x, y)

demo()

x = [1,2,3]
y=x
y.append(4)

# print(x)  # [1, 2, 3, 4]


# Stack | Heap
# x,y     [1,2,3]
# ----------^




# Disassembling Bytecode

import dis

def add(a,b):
    print(f"Adding numbers: {a} and {b}")
    return a + b

dis.dis(add)




