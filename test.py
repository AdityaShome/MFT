```python
import random
import os

def division_error():
    """
    Simulates division by randomly choosing a denominator that might be zero.
    If the denominator is zero, it catches the ZeroDivisionError and prints an error message.
    Returns the result of the division if successful, or None if an error occurred.
    """
    numerator = random.randint(1, 10)
    try:
        denominator = random.choice([0, random.randint(1, 10)])  # Sometimes will divide by 0
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

def file_read_error():
    """
    Attempts to read a file that may not exist.
    If the file doesn't exist, it catches the FileNotFoundError and prints an error message.
    If the file is read successfully, it prints the content of the file.
    """
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")

# Example usage
if __name__ == "__main__":
    print(division_error())
    file_read_error()
```