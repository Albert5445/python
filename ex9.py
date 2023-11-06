#Write a function that gets a number, not a negative integer, and subtract all its odd digits. If all digits are subtracted,
#return zero.

def subtract_odd_numbers(numbers):

    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

result = subtract_odd_numbers(numbers)
print(result)

