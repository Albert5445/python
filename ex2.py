#calc with functions

def gumarum(a,b):
    print(f"Answer is {a+b}")

def bajanum(a,b):
    print(f"Answer is {a//b}")

def hanum(a,b):
    print(f"Answer is {a-b}")

def bazmapatkum(a,b):
    print(f"Answer is {a*b}")

act1 = {"+": gumarum,
         "-": hanum,
         "//": bajanum,
         "*": bazmapatkum}
def calculate(act1):
    val = act1.get(a, b, act1)
    return f'Answer {val}'


a = int(input("Give a first numbr "))
b = int(input("Give a second numbr "))
act = input('Action')
print(calculate(act))

