
def calculate_factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        number (int): The number whose factorial is calculated.

    Returns:
        int: The factorial of the given number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Input must be an integer")

    if number < 0:
        raise ValueError("Number must be non-negative")

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial


try:
    number = int(input("Enter a non-negative integer: "))
    result = calculate_factorial(number)
    print(f"Factorial of {number} is {result}")

except ValueError as error:
    print(f"Error: {error}")
except TypeError as error:
    print(f"Error: {error}")
