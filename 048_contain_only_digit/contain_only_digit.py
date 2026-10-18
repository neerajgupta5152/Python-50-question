
def contains_only_digits(my_string: str) -> bool:
    """
    Check whether a string contains only digits.

    Args:
        my_string (str): The input string.

    Returns:
        bool: True if all characters are digits, otherwise False.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string is empty.
    """
    # Check input type
    if not isinstance(my_string, str):
        raise TypeError("Input must be a string.")

    # Check empty string
    if not my_string:
        raise ValueError("String cannot be empty.")

    # Check each character
    for char in my_string:
        if char < "0" or char > "9":
            return False

    return True


def main():
    try:
        my_string = "123456"
        print(contains_only_digits(my_string))

        my_string = "123a56"
        print(contains_only_digits(my_string))

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
