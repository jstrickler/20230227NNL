

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    return 42
    # If no return statement, return None


x = say_hello()  # Call function (arguments, if any, in () )
print(f"x: {x}")


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()
import typing as T
Number = T.Union[int, float]

value: str = "abc"


value = 27

def sqrt(num: Number) -> float:  # Function takes exactly one argument
    """
    Calculate the square root of a number.

    Parameters

    :num: any int or float
    :return: square root as a float
    """
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
# x = sqrt('m')

print("m is {:.3f} n is {:.3f}".format(m, n))

