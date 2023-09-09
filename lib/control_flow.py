#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
     return "It's perfect out there!"
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Invalid operation! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation!"
    pass


print(admin_login("sudo", "12345"))  # "Access denied"
print(admin_login("admin", "12345"))  # "Access granted"
print(hows_the_weather(33))  # "It's brisk out there!"
print(hows_the_weather(99))  # "It's too dang hot out there!"
print(fizzbuzz(1))  # 1
print(fizzbuzz(3))  # "Fizz"
print(calculator("+", 1, 1))  # 2
print(calculator("nope", 4, 2))  # "Invalid operation!"