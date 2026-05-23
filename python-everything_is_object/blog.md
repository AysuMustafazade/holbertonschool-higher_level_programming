# Python3: Mutable, Immutable… Everything is Object!

## Introduction

If you're learning Python, one of the most important — and often misunderstood — concepts is how Python treats **everything as an object**. Whether it's a number, a string, a list, or even a function, Python wraps it in an object with an identity, a type, and a value. Understanding this deeply changes how you write, debug, and reason about Python code. Two of the most critical distinctions you'll encounter are **mutability** and **immutability**: whether an object's value can be changed after it's created. In this post, we'll walk through `id()` and `type()`, the difference between mutable and immutable objects, why it matters, and how Python handles passing objects to functions.

---

## `id()` and `type()`

Every object in Python has three key properties: an **identity** (its memory address), a **type** (what kind of object it is), and a **value** (the data it holds). You can inspect these using the built-in `id()` and `type()` functions.

```python
x = 42
print(id(x))      # e.g. 140245639969392
print(type(x))    # <class 'int'>

name = "Alice"
print(id(name))   # e.g. 140245622130736
print(type(name)) # <class 'str'>

items = [1, 2, 3]
print(id(items))  # e.g. 140245615232640
print(type(items)) # <class 'list'>
```

The `id()` function returns a unique integer that identifies the object — in CPython, this is its memory address. Two variables can point to the **same** object (same `id`) or to **different** objects with equal values (different `id`). This distinction is checked using `is` (identity) vs `==` (equality):

```python
a = [1, 2, 3]
b = a           # b and a point to the same object
c = [1, 2, 3]   # c is a new object with the same value

print(a == c)   # True  — same value
print(a is c)   # False — different objects
print(a is b)   # True  — same object

print(id(a))    # e.g. 140245615232640
print(id(b))    # same as id(a)
print(id(c))    # different
```

> **Key takeaway:** `==` compares values; `is` compares identity (memory address).

---

## Mutable Objects

A **mutable** object is one whose value can be changed **in place** after it's created — without creating a new object. The most common built-in mutable types are:

- `list`
- `dict`
- `set`
- `bytearray`

```python
# Lists are mutable
fruits = ["apple", "banana"]
print(id(fruits))       # e.g. 140245615232640

fruits.append("cherry")
print(fruits)           # ['apple', 'banana', 'cherry']
print(id(fruits))       # Same id! The object was modified in place.
```

```python
# Dicts are mutable
person = {"name": "Bob", "age": 30}
print(id(person))       # e.g. 140245615199680

person["age"] = 31
print(person)           # {'name': 'Bob', 'age': 31}
print(id(person))       # Same id — modified in place
```

```python
# Sets are mutable
s = {1, 2, 3}
print(id(s))            # e.g. 140245610278720
s.add(4)
print(s)                # {1, 2, 3, 4}
print(id(s))            # Same id
```

Since mutable objects can be changed in place, two variables pointing to the same mutable object will **both see the change**:

```python
a = [10, 20, 30]
b = a               # b is an alias for a

b.append(40)
print(a)            # [10, 20, 30, 40] — a changed too!
print(a is b)       # True
```

---

## Immutable Objects

An **immutable** object cannot be changed after it's created. If you try to "modify" it, Python creates a **new object** instead. The most common built-in immutable types are:

- `int`
- `float`
- `str`
- `tuple`
- `bool`
- `frozenset`
- `bytes`

```python
# Integers are immutable
x = 10
print(id(x))   # e.g. 140245639969072

x += 1
print(x)       # 11
print(id(x))   # Different id — a new object was created!
```

```python
# Strings are immutable
s = "hello"
print(id(s))   # e.g. 140245622130736

s += " world"
print(s)       # hello world
print(id(s))   # Different id — new string object
```

```python
# Tuples are immutable
t = (1, 2, 3)
# t[0] = 99  # This would raise: TypeError: 'tuple' object does not support item assignment
```

> **Note:** A tuple containing a mutable object (like a list) is itself immutable — you can't reassign elements — but the mutable object *inside* can still be changed:

```python
t = ([1, 2], "hello")
t[0].append(3)
print(t)       # ([1, 2, 3], 'hello') — the list inside changed!
```

Python sometimes **interns** (reuses) small integers and short strings as an optimization:

```python
a = 256
b = 256
print(a is b)   # True — CPython caches small ints (-5 to 256)

c = 257
d = 257
print(c is d)   # False — outside the cache range
```

---

## Why Does It Matter? How Python Treats Mutable and Immutable Objects Differently

The mutable/immutable distinction has real consequences for how your code behaves, especially around **aliasing**, **copying**, and **default arguments**.

**Aliasing:** With mutable objects, two variable names can refer to the same underlying object. Changing one changes the other. With immutable objects, reassignment always creates a new object — the original is never touched.

```python
# Mutable aliasing — dangerous if unintended
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
print(list1)    # [99, 2, 3] — list1 was affected!

# Immutable — safe
x = 5
y = x
y += 1
print(x)        # 5 — x is unchanged
```

**Copying:** To avoid aliasing bugs with mutable objects, use `.copy()` or `copy.deepcopy()`:

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()       # Shallow copy — inner lists still shared
deep = copy.deepcopy(original)  # Deep copy — fully independent

shallow[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]] — shallow copy affected original!
print(deep)      # [[1, 2], [3, 4]]     — deep copy is unaffected
```

**Mutable default arguments — a classic Python gotcha:**

```python
# BAD: mutable default argument
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b'] — the default list persists!

# GOOD: use None and create a new list each call
def add_item_safe(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_safe("a"))  # ['a']
print(add_item_safe("b"))  # ['b']
```

---

## How Arguments Are Passed to Functions — and What It Implies for Mutable and Immutable Objects

Python passes arguments using a model sometimes called **"pass by object reference"** (or "pass by assignment"). This means: the function receives a **reference to the same object**, not a copy of the value.

What happens next depends on whether the object is mutable or immutable.

**With immutable objects**, since the object can't be changed in place, any "modification" inside the function creates a new local object. The original variable outside the function is **unaffected**:

```python
def double(n):
    print(f"Inside before: id={id(n)}, value={n}")
    n *= 2
    print(f"Inside after:  id={id(n)}, value={n}")

x = 10
print(f"Outside before: id={id(x)}, value={x}")
double(x)
print(f"Outside after:  id={id(x)}, value={x}")

# Output:
# Outside before: id=140245639969072, value=10
# Inside before:  id=140245639969072, value=10
# Inside after:   id=140245639969232, value=20   ← new object
# Outside after:  id=140245639969072, value=10   ← unchanged!
```

**With mutable objects**, since the function receives a reference to the same object, in-place modifications **do affect** the original:

```python
def append_zero(lst):
    print(f"Inside before: id={id(lst)}, value={lst}")
    lst.append(0)
    print(f"Inside after:  id={id(lst)}, value={lst}")

my_list = [1, 2, 3]
print(f"Outside before: id={id(my_list)}, value={my_list}")
append_zero(my_list)
print(f"Outside after:  id={id(my_list)}, value={my_list}")

# Output:
# Outside before: id=140245615232640, value=[1, 2, 3]
# Inside before:  id=140245615232640, value=[1, 2, 3]
# Inside after:   id=140245615232640, value=[1, 2, 3, 0]  ← same object
# Outside after:  id=140245615232640, value=[1, 2, 3, 0]  ← changed!
```

However, **reassigning** the parameter variable inside the function does NOT affect the caller — it just rebinds the local name to a new object:

```python
def replace_list(lst):
    lst = [99, 100]   # local rebinding — not the same as lst.clear(); lst.extend(...)
    print(f"Inside: {lst}")

my_list = [1, 2, 3]
replace_list(my_list)
print(f"Outside: {my_list}")  # [1, 2, 3] — unchanged!
```

**Summary table:**

| Object type | Passed as | In-place change affects caller? | Reassignment affects caller? |
|-------------|-----------|----------------------------------|------------------------------|
| Immutable (`int`, `str`, `tuple`) | Reference | N/A (can't change in place) | No |
| Mutable (`list`, `dict`, `set`) | Reference | **Yes** | No |

---

## Conclusion

Understanding that everything in Python is an object, and grasping the difference between mutable and immutable objects, is foundational to writing correct Python code. Use `id()` to inspect object identity, use `is` to check if two names refer to the same object, be cautious with mutable defaults in functions, and always be aware that passing a mutable object to a function gives that function the power to modify it. These concepts will help you avoid subtle bugs and write more predictable, readable Python.

