# Codomax Internship - Module 1
# Python Functions

# Simple function
def greet(name):
    print("Hello,", name)


greet("Sabreen")


# Function with calculation
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Sum:", result)


# Function to check even or odd
def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is:", check_number(10))
print("7 is:", check_number(7))
