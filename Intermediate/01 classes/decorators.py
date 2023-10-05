# functions are objects
def add_five(num):
    print(num+5)

add_five(2)
print(add_five)

# functions within functions
def add_five2(num):
    def add_two(num):
        return num + 2
    num_plus_two = add_two(num)


add_five2(5)

# returning functions from functions
def get_math_function(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    if operation=='+':
        return add
    elif operation=='-':
        return sub

add_function = get_math_function('+')
print(add_function)
print(add_function(4,6))

# decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

def print_my_name():
    print("Me")

print_my_name()
decorated_function = title_decorator(print_my_name)
decorated_function()

# decorators
def title_decorator2(print_name_function):
    def wrapper2():
        print("(decorated) Professor:")
        print_name_function()
    return wrapper2

@title_decorator2
def print_my_name2():
    print("Me")

print_my_name2()

# decorators with parameters
def title_decorator3(print_name_function):
    def wrapper3(*args, **kwargs):
        print("(decorated3) Professor:")
        print_name_function(*args, **kwargs)
    return wrapper3

@title_decorator3
def print_my_name3(name):
    print(name)

print_my_name3("shelby")