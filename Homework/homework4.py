#     # TODO #1: Account for `kwargs` and sum all the numbers in there
def sum_numbers(*args, **kwargs):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
    for val in kwargs.values():
        if isinstance(val, (int, float)):
            total_sum += val
    return total_sum

print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))

#     # TODO #2: Account for every number at any level in both `args` and `kwargs`

def sum_numbers(*args, **kwargs):
    def add_numbers(numbers):
        total_sum = 0
        for num in numbers:
            if isinstance(num, (int, float)):
                total_sum += num
            elif isinstance(num, (list, tuple)):
                total_sum += add_numbers(num)
            elif isinstance(num, dict):
                total_sum += add_numbers(num.values())
        return total_sum

    total_sum = 0

    total_sum += add_numbers(args)
    total_sum += add_numbers(kwargs.values())

    return total_sum

print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))