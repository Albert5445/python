def counting_digits(number):
    num_str = str(number)
    return len(num_str)

num = int(input("enter the number: "))

print("number of digits", counting_digits(num))