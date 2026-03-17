# Python Basics: if/else, Loops, Functions

## Overview
Basic concepts of Python: conditionals, loops, functions, and syntax.

## 1. Indentation
Defines code blocks.
```python
if True:
    print("Correct")

```
## 2. Conditionals
```
if x > 0:
    print("Positive")
else:
    print("Negative")
```

## 3. Comments
```
# This is a comment
```
## 4. Variables
```
x = 10
name = "Python"
```
## 5. Loops
```
for i in range(3):
    print(i)

while x > 0:
    x -= 1
```    
## 6. break / continue
```
for i in range(5):
    if i == 3:
        break
```        
## 7. Loop else
```
for i in range(3):
    print(i)
else:
    print("Done")
```
## 8. pass
```
if True:
    pass
```    
## 9. range()
```
range(5)
```
## 10. Functions
```
def greet():
    return "Hello"
```    
## 11. Return
```
def test():
    pass  # returns None
```    
## 12. Scope
```
x = 10
def f():
    x = 5
```    
## 13. Traceback
```
NameError: name 'x' is not defined
```
## 14. Operators
```
+ - * / // % **
```