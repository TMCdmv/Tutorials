"""
Pythom programming example
"""

from functools import wraps
import pendulum


def timer(func):
    """
    Simple Decorator to measure a function execution time.
    """

    @wraps(func)
    def function_wrapper():
        """
        decorator example
        """
        start = pendulum.now()
        func()
        elapsed_time = pendulum.now() - start
        print(f"Execution Time: {elapsed_time.microseconds} ms.")

    return function_wrapper


@timer
def test_function():
    """
    decorator example
    """
    for i in range(100000):
        total = 0
        total += i


test_function()
