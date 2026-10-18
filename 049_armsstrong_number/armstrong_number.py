
def is_armstrong(number: int) -> bool:
    """
    Check whether a number is an Armstrong number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is Armstrong, otherwise False.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If the number is negative.
    """
    # Check input type
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Input must be an integer.")

    # Check negative number
    if number < 0:
        raise ValueError("Number cannot be negative.")

    # Count the digits
    digits = str(number)
    power = len(digits)
    result = 0

    # Calculate the sum of digits raised to the power
    for digit in digits:
        result += int(digit) ** power

    # Compare the result with the original number
    return result == number


def main():
    try:
        number = 153
        print(is_armstrong(number))

        number = 123
        print(is_armstrong(number))

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
