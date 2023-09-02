
#Enter three integers from the keyboard. Decide which is the biggest.


a = int(input("Give the first number: "))
b = int(input("Give the second number: "))
c = int(input("Give the third number: "))
if a>b and a>c :
    print(f"the biggest is {a}")
elif b>a and b>c :
    print(f"the biggest is {b}")
elif c>a and c>b :
    print(f"the biggest is {c}")
else:
    print("something is wrong")