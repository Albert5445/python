import math
# print("1. Gumarum")
# print("2. Hanum")
# print("3. Bazmapatkum")
# print("4. Bajanum")
action = input("Chose the action: ")

if action == '+' :
    print("+")
    a = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    c = a+b
    print(c)
elif action == '-':
    print("-")
    a = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    c = a - b
    print(c)
elif action == '/':
    print("/")
    a = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    c = a // b
    print(c)
elif action == '*':
    print("*")
    a = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    c = a * b
    print(c)
else:
    print("Something get wrong")