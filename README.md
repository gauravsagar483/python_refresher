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


## Asyncio Python: Episode 3

```
This episode focuses on the `asyncio` library in Python, which is used for writing asynchronous programs. The `asyncio` module provides a framework for managing asynchronous I/O, coroutines, tasks, and event loops, enabling developers to write highly concurrent code.
```
### Prerequisites

- Basic understanding of Python functions and control flow.
- Familiarity with synchronous programming concepts like loops and exception handling. 


### Key Concepts Covered

#### 1. **Event Loop**
    - The core of `asyncio`, responsible for executing asynchronous tasks and managing I/O operations.
    - The event loop runs until all tasks are completed or explicitly stopped.

#### 2. **Coroutines**
    - Special functions defined using `async def` that can be paused and resumed.
    - Coroutines are the building blocks of asynchronous programming in Python.

#### 3. **Tasks & Tasks Groups**
    - A higher-level abstraction for managing coroutines.
    - Created using `asyncio.create_task()` to schedule coroutines for execution.

#### 4. **Awaitables, Cancel and Timeouts**
    - Objects that can be awaited using the `await` keyword.
    - Includes coroutines, tasks, and objects implementing the `__await__()` method.

#### 5. **Asynchronous I/O**
    - Non-blocking I/O operations, such as reading from or writing to files, sockets, or other streams.
    - Allows the program to perform other tasks while waiting for I/O operations to complete.

#### 6. **Concurrency with asyncio vs Parellalism**
    - Enables running multiple coroutines concurrently using `asyncio.gather()` or `asyncio.wait()`.
    - Useful for tasks like making multiple API calls or processing multiple files simultaneously.

#### 6. **Interview questions answered.**
    - Answered some of the most asked question for you in the video on the asyncio

### Example Topics in the Code


- **Defining and Running Coroutines**: Shows how to define `async def` functions and execute them using `await`.
- **Using `asyncio.sleep()`**: Introduces the concept of pausing execution for a specified duration.
- **Handling Exceptions in Coroutines**: Explains how to catch and handle exceptions raised within coroutines.
- **Combining Multiple Coroutines**: Illustrates how to run multiple coroutines concurrently and collect their results.



### Additional Resources

- [Python Official Documentation on asyncio](https://docs.python.org/3/library/asyncio.html)


This episode provides a hands-on introduction to `asyncio`, helping you understand how to write efficient and scalable asynchronous programs in Python.