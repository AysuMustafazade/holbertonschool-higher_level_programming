# Python - Exceptions

## Description
This project covers the fundamentals of error handling in Python. Understanding the difference between syntax errors and exceptions is crucial for writing robust, "bulletproof" code that can gracefully handle unexpected situations without crashing.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:

### General
* **Why Python programming is awesome:** Its readability, vast standard library, and elegant approach to error handling through "Easier to Ask for Forgiveness than Permission" (EAFP).
* **Errors vs. Exceptions:** * **Errors** (usually Syntax Errors) occur when the parser detects an incorrect statement before the code even runs.
    * **Exceptions** occur during execution when the code is syntactically correct but results in an error (e.g., `ZeroDivisionError` or `TypeError`).
* **What are Exceptions:** Objects that represent an error that occurred during the execution of a program.
* **Correctly handling Exceptions:** Using `try`, `except`, `else`, and `finally` blocks.
* **Purpose of catching Exceptions:** To prevent the program from crashing and to provide meaningful feedback or alternative logic when something goes wrong.
* **Raising Built-in Exceptions:** Using the `raise` keyword to force a specific exception to occur.
* **Clean-up Actions:** Using the `finally` block to ensure resources (like files or network connections) are closed regardless of whether an exception was raised.
