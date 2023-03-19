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
    total_sum = 0

    # Iterate through args
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, (list, tuple)):
            total_sum += sum_numbers(*arg)
        elif isinstance(arg, dict):
            total_sum += sum_numbers(*arg.values())

    # Iterate through kwargs
    for val in kwargs.values():
        if isinstance(val, (int, float)):
            total_sum += val
        elif isinstance(val, (list, tuple)):
            total_sum += sum_numbers(*val)
        elif isinstance(val, dict):
            total_sum += sum_numbers(*val.values())

    return total_sum

print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))