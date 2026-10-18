
def first_non_repeated(my_string: str) -> str:
    """
    Return the first non-repeated character in a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The first non-repeated character.

    Raises:
        TypeError: If input is not a string.
        ValueError: If string is empty or has no non-repeated character.
    """
    # Check input type
    if not isinstance(my_string, str):
        raise TypeError("Input must be a string.")

    # Check empty string
    if not my_string:
        raise ValueError("String cannot be empty.")

    # Check each character
    for char in my_string:
        if my_string.count(char) == 1:
            return char

    # If no unique character is found
    raise ValueError("No non-repeated character found.")


def main():
    try:
        my_string = "swiss"
        result = first_non_repeated(my_string)
        print(result)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
