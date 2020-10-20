#  '*' is used for unpicking arguments
# * can be used in function defining for collecting arguments
# and it can be used while calling function for unpacking arguments


def multiply(*args):
    print(args)
    total = 1
    for n in args:
        total *= n
    return total


print(multiply(1, 3, 5))


# destructuring arguments
# single * for unpacking list as argument
def add(x, y):
    return x + y


nums = [2, 5]
print(add(*nums))

# double * for unpacking dictionaries
my_dict = {'x': 3, 'y': 5}
print(add(**my_dict))


# cal

def calculator(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "Use valid operator."


print(calculator(1, 2, 3, 4, 5, operator='*'))


# * - positional arguments, ** - named arguments

def done(*args, **kwargs):
    print(args)
    print(kwargs)


done(1, 23, 4, name='Pratik', age=20)

