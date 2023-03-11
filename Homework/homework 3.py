def sum_numbers(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
    return total_sum
print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc'))

def sum_of_all_numbers(n):
    if n < 0:
        return 0
    if n == 0:
        return 0
    return n + sum_of_all_numbers(n-1)

def sum_of_even_numbers(n):
    if n < 0:
        return 0
    if n < 2:
        return 0
    if n % 2 != 0:
        n -= 1
    return n + sum_of_even_numbers(n-2)

def sum_of_odd_numbers(n):
    if n < 1:
        return 0
    if n % 2 == 0:
        n -= 1
    return n + sum_of_odd_numbers(n-2)
print("Sum of all numbers is: ",sum_of_all_numbers(5))
print("Sum of all even numbers is: ",sum_of_even_numbers(5))
print("Sum of all odd numbers is: ",sum_of_odd_numbers(5))

def read_integer():
    value = input("Enter an integer: ")
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        return 0
print(read_integer())





