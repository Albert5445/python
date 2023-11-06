#In the entered interval of natural numbers, find those whose number of divisors is not less than the entered value.
#For the found numbers, display the number of divisors and all divisors.

def count_divisors(num):
    count = 0
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            divisors.append(i)
    return count, divisors

def divisors(min_value, max_value, min_divisor_count):
    numbers = []
    for num in range(min_value, max_value + 1):
        divisor_count, divisors = count_divisors(num)
        if divisor_count >= min_divisor_count:
            numbers.append((num, divisor_count, divisors))
        return numbers

min_value = int(input("Enter the min value "))
max_value = int(input("Enter the max value "))
min_divisor_count = int(input("min number of divisors "))

result = divisors(min_value, max_value, min_divisor_count)

if not result:
    print("No numbers found with at least", min_divisor_count, "divisors.")
else:
    for num, divisor_count, divisors in result:
        print(f"Number: {num}, Divisor Count: {divisor_count}, Divisors: {divisors}")

