# 🔄 Python — Swap Two Numbers (3 Methods)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
![Level](https://img.shields.io/badge/Level-Beginner-yellow?style=flat-square)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-36-lightgrey?style=flat-square)

A beginner-friendly Python program demonstrating **three distinct approaches** to swap two numbers — from the intuitive temporary variable method to the elegant XOR bitwise technique.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Methods Covered](#methods-covered)
  - [Method 1 — Temporary Variable](#method-1--temporary-variable)
  - [Method 2 — Addition & Subtraction](#method-2--addition--subtraction)
  - [Method 3 — XOR Bitwise Operation](#method-3--xor-bitwise-operation)
- [Sample Output](#sample-output)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [Concepts Learned](#concepts-learned)
- [Author](#author)

---

## Project Overview

Swapping two variables is one of the most fundamental operations in programming. This project explores **three different ways** to achieve it in Python, each highlighting a different concept — from basic variable assignment to arithmetic manipulation and low-level bitwise logic.

Each method is implemented as a separate function with a **docstring** that explains its logic, making the code clean, readable, and educational.

---

## Methods Covered

### Method 1 — Temporary Variable

The most straightforward and commonly taught approach. A third `temp` variable holds one value while the swap takes place.

```python
def tempvar(a, b):
    """using temporary variable to swap two numbers"""
    temp = a
    a = b
    b = temp
    print(f'a is {a} b is {b}')
```

**Concept:** Basic variable assignment  
**Pros:** Highly readable and easy to understand  
**Cons:** Uses an extra variable in memory

---

### Method 2 — Addition & Subtraction

Swaps two numbers using arithmetic — no extra variable needed. Works by encoding both values into `a` using addition, then unpacking them.

```python
def addsub(a, b):
    """using addition and subtraction to swap two numbers"""
    a = a + b
    b = a - b
    a = a - b
    print(f'a is {a} b is {b}')
```

**Concept:** Arithmetic manipulation  
**Pros:** No extra variable required  
**Cons:** Risk of integer overflow for very large numbers

---

### Method 3 — XOR Bitwise Operation

The most efficient and low-level approach. Uses the XOR (`^`) bitwise operator — a value XORed with itself is always `0`, and XOR is self-inverse.

```python
def bitwiseops(a, b):
    """using XOR to swap two vars"""
    a = a ^ b
    b = b ^ a
    a = a ^ b
    print(f'a is {a} b is {b}')
```

**Concept:** Bitwise XOR operation  
**Pros:** No extra memory, works at the bit level  
**Cons:** Less readable; only works with integers

---

## Sample Output

```
 a : 5
 b : 10

a is 10 b is 5
using temporary variable to swap two numbers

a is 10 b is 5
using addition and subtraction to swap two numbers

a is 10 b is 5
using XOR to swap two vars
```

---

## How to Run

**Prerequisites:** Python 3.x installed on your system.

**Steps:**

```bash
# 1. Clone the repository
git clone https://github.com/thekavyaasharma/python-swap-two-numbers.git

# 2. Navigate into the directory
cd python-swap-two-numbers

# 3. Run the script
python swaptwonumber.py
```

The program will prompt you to enter two integers, then display the swapped result using all three methods.

---

## File Structure

```
python-swap-two-numbers/
│
├── swaptwonumber.py    # Main Python script with all 3 swap methods
└── README.md           # Project documentation
```

---

## Concepts Learned

- Defining and calling functions in Python
- Writing and accessing **docstrings** with `__doc__`
- Variable assignment and temporary storage
- Arithmetic-based variable manipulation
- Bitwise XOR (`^`) operator and its properties
- Taking user input with `int(input())`
- f-string formatting for output

---

## Author

**Kavya Sharma**  
B.Tech CSE (2nd Year)

Feel free to reach out for feedback, collaboration, or discussion!

[![GitHub](https://img.shields.io/badge/GitHub-thekavyaasharma-181717?style=flat-square&logo=github)](https://github.com/thekavyaasharma)
