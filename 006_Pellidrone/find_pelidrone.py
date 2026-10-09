
def check_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome using a for loop.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the string is empty.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text:
        raise ValueError("String cannot be empty")

    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse


try:
    string = input("Enter a string: ")

    if check_palindrome(string):
        print("String is a palindrome.")
    else:
        print("String is not a palindrome.")

except (TypeError, ValueError) as error:
    print(f"Error: {error}")
