# Minimum Operations

## Project Overview
This project implements a Python function `minOperations(n)` that calculates the **minimum number of operations** needed to produce exactly `n` characters `'H'` in a text file. The operations allowed are:

1. **Copy All** – copies all characters currently in the file.
2. **Paste** – pastes the characters previously copied.

The goal is to start with a single `'H'` and use the fewest possible operations to reach exactly `n` characters.

---

## Function Prototype
```python
def minOperations(n):
    """
    Calculate the minimum number of operations to reach n 'H' characters.
    
    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Minimum number of operations, or 0 if n is impossible to achieve.
    """
