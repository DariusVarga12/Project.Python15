def sum_numbers(*args, **kwargs):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
    return total_sum
print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))

def get_rec_sum(n: int) -> tuple:
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = get_rec_sum(n - 1)

    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


total_sum, even_sum, odd_sum = get_rec_sum(5)
print("total_sum", total_sum)
print("even_sum", even_sum)
print("odd_sum", odd_sum)



def get_integer_from_input():
    user_input = input("Input: ")

    try:
        return int(user_input)
    except ValueError:
        return 0


print(get_integer_from_input())

