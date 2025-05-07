# python_refresher
Refresher guide for Python devs




## Python Refresher: Episode 1

Welcome to the first episode of the Python refresher series! 🚀 This episode covers essential Python concepts, ranging from data structures to advanced topics like decorators and asyncio. Let's dive in!

---

### 📚 Topics Covered

#### 1. **Data Structures and Their Mutability**
Python data structures can be categorized into **immutable** and **mutable** types.

- **Immutable** ❌
    - Examples: `Number`, `Boolean`, `String`, `Tuple`, `Bytes`, `Frozen Sets`
    - Once created, their values cannot be changed.
    ```python
    x = "Hello"
    # x[0] = "J"  # ❌ TypeError: 'str' object does not support item assignment
    assert x[0] == "H"
    ```

- **Mutable** ✅
    - Examples: `List`, `Set`, `Dict`, `Byte Arrays`
    - Their values can be modified after creation.
    ```python
    arr = [1, 2, 3, 4, 5]
    arr[0] = 10
    assert arr[0] == 10
    ```

- **Interesting Case: Tuples**
    - Tuples are immutable, but if they contain mutable objects, those objects can be modified.
    ```python
    tup = ("hello", [1, 2, 3])
    tup[1][0] = 10  # ✅
    assert tup[1][0] == 10
    ```

---

#### 2. **Type Hinting**
Type hinting improves code readability and helps IDEs provide better support. However, it is not enforced at runtime.


## Python Refresher: Episode 2

### 📚 Topics Covered

This script explores how Python works under the hood, covering topics like Abstract Syntax Tree (AST), Global Interpreter Lock (GIL), bytecode, memory management, and CPython. Below is an overview of the concepts and code snippets included in the file.

---

#### **Abstract Syntax Tree (AST)**

Python first parses your code into an Abstract Syntax Tree (AST) before compiling it into bytecode. The `ast` module is used to parse and inspect the AST representation of Python code.


#### **Global Interpreter Lock (GIL)**

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecode simultaneously. This simplifies memory management but can be a bottleneck for CPU-bound tasks.

- **Key Points**:
    - Only one thread executes Python bytecode at a time.
    - Useful for I/O-bound tasks but limits multi-threading for CPU-bound tasks.
    - Workarounds include multiprocessing or using libraries like `numba` or `cython`.

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Output may not be 2000000 due to GIL
```

---

#### **Bytecode**

Python code is compiled into bytecode, which is a low-level, platform-independent representation of your source code. The bytecode is executed by the Python Virtual Machine (PVM).

- **Inspecting Bytecode**:
    Use the `dis` module to disassemble Python functions and inspect their bytecode.

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

---

#### **Memory Management**

Python uses automatic memory management, including garbage collection, to manage memory allocation and deallocation.

- **Key Features**:
    - Reference counting: Objects are deallocated when their reference count drops to zero.
    - Garbage collection: Handles cyclic references using the `gc` module.

```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Creates a reference cycle

del a
del b

gc.collect()  # Explicitly trigger garbage collection
```

---

#### **CPython**

CPython is the default and most widely used implementation of Python. It is written in C and serves as both an interpreter and a runtime environment.

- **Key Features**:
    - Converts Python code to bytecode and executes it.
    - Provides a C API for extending Python with C/C++ modules.
    - Basis for other implementations like PyPy and Jython.

- **Example: Extending Python with C**:
    You can write performance-critical code in C and integrate it with Python using CPython's API.

```c
#include <Python.h>

static PyObject* add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

static PyMethodDef methods[] = {
    {"add", add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "example",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&module);
}
```

Compile the above C code into a shared library and import it in Python:

```python
import example
print(example.add(2, 3))  # Output: 5
```