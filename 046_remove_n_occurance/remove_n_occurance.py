
def remove_nth_occurrence(my_string: str, char: str, n: int) -> str:
    """
    Remove the nth occurrence of a character from a string.

    Args:
        my_string (str): The input string.
        char (str): The character to remove.
        n (int): The occurrence number to remove.

    Returns:
        str: The string after removing the nth occurrence.

    Raises:
        TypeError: If the input types are invalid.
        ValueError: If the string, character, or n is invalid.
    """
    # Exception handling: validate input types
    if not isinstance(my_string, str):
        raise TypeError("Input string must be a string.")

    if not isinstance(char, str):
        raise TypeError("Character must be a string.")

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    # Validate input values
    if not my_string:
        raise ValueError("String cannot be empty.")

    if len(char) != 1:
        raise ValueError("Character must contain exactly one character.")

    if n <= 0:
        raise ValueError("n must be greater than zero.")

    count = 0
    result = ""

    # Check each character in the string
    for letter in my_string:
        if letter == char:
            count += 1

            # Skip the nth occurrence
            if count == n:
                continue

        result += letter

    # Check whether the requested occurrence exists
    if count < n:
        raise ValueError("The requested occurrence does not exist.")

    return result


def main():
    try:
        my_string = "example example example"
        char = "e"
        n = 2

        result = remove_nth_occurrence(my_string, char, n)
        print(result)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
