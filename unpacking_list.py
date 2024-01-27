# Certainly! Here's a simple Python example using the * operator for argument unpacking:

# Function that takes multiple arguments
def add_numbers(a, b, c):
    return a + b + c


# List of values
numbers = [1, 2, 3]

# Without unpacking
result_without_unpacking = add_numbers(numbers[0], numbers[1], numbers[2])
print("Result without unpacking:", result_without_unpacking)

# With unpacking using *
result_with_unpacking = add_numbers(*numbers)
print("Result with unpacking:", result_with_unpacking)
