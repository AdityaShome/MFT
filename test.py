# errornomous.py

import random
import os

# Function to simulate division errors
def division_error():
    numerator = random.randint(1, 10)
    denominator = random.choice([0, random.randint(1, 10)])  # Sometimes will divide by 0
    result = numerator / denominator
    return result

# Function to simulate file reading errors
def file_read_error():
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found error triggered.")

# Function to simulate attribute errors
def attribute_error():
    obj = None
    try:
        obj.some_method()  # NoneType object has no attribute 'some_method'
    except AttributeError:
        print("AttributeError triggered.")

# Function to simulate value errors
def value_error():
    try:
        int("Not a number")  # Trying to convert a non-numeric string to an integer
    except ValueError:
        print("ValueError triggered.")

# Function to simulate index errors
def index_error():
    try:
        lst = [1, 2, 3]
        return lst[5]  # Index out of range
    except IndexError:
        print("IndexError triggered.")

# Function to simulate key errors in dictionaries
def key_error():
    try:
        my_dict = {"name": "John", "age": 30}
        print(my_dict["address"])  # Key 'address' does not exist
    except KeyError:
        print("KeyError triggered.")

# Function to simulate type errors
def type_error():
    try:
        result = "hello" + 5  # Trying to add a string and an integer
    except TypeError:
        print("TypeError triggered.")

# Simulate all the errors in one function
def simulate_all_errors():
    print("Simulating errors...")
    division_error()
    file_read_error()
    attribute_error()
    value_error()
    index_error()
    key_error()
    type_error()

# Main execution
if __name__ == "__main__":
    simulate_all_errors()

    # Adding a hanging function to simulate an infinite loop (optional)
    while True:
        user_input = input("Enter 'exit' to stop or any key to continue: ")
        if user_input.lower() == "exit":
            break
        else:
            print("Continuing...")

    # End of the script, just to make sure something ends properly
    print("Script execution finished.")
