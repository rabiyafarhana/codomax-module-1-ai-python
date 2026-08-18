# Codomax Internship - Module 1
# Beginner Python Programs


# 1. Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# 2. Find the largest of two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number:", a)
else:
    print("Largest number:", b)


# 3. Simple calculator
num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
