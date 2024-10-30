# Python Functions Example

# The len() function returns the number of items in an object.
# For a list, it returns the number of elements in that list.

# Example of using len() to find the length of a list
my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print(f"The length of the list is: {list_length}")  # Output: 5

# Function to greet a person by name
def greet(name):
    print(f"Hello, {name}!")

# Example usage of greet function
greet("Alice")  # Output: Hello, Alice!

# Function to find the maximum value in a list of integers without using max()
def find_maximum(numbers):
    # Assume the first number is the maximum initially
    maximum_value = numbers[0]
    # Loop through the list and update maximum_value if a larger number is found
    for number in numbers:
        if number > maximum_value:
            maximum_value = number
    return maximum_value

# Example usage of find_maximum function
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value = find_maximum(numbers_list)
print(f"The maximum value in the list is: {max_value}")  # Output: 9

# Explanation of local and global variables:
# Local variables are defined within a function and can only be accessed there.
# Global variables are defined outside any function and can be accessed anywhere in the code.

# Example demonstrating local and global variables
global_var = "I am a global variable"

def example_function():
    local_var = "I am a local variable"
    print(local_var)  # This will work, as local_var is defined in this scope
    print(global_var)  # This will work, as global_var is defined outside the function

example_function()
print(global_var)  # This will work
# print(local_var)  # This would raise an error because local_var is not accessible here

# Function to calculate the area of a rectangle
def calculate_area(length, width=5):
    return length * width

# Example usage of calculate_area function
area_with_default_width = calculate_area(10)
area_with_custom_width = calculate_area(10, 7)

print(f"Area with default width: {area_with_default_width}")  # Output: 50
print(f"Area with custom width: {area_with_custom_width}")    # Output: 70
