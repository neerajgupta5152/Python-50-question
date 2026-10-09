
def count_vowels(text: str) -> int:
    """
    Count vowels in a string, ignoring uppercase and lowercase differences.

    Args:
        text (str): The input string.

    Returns:
        int: The total number of vowels.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


try:
    string = input("Enter a string: ")
    result = count_vowels(string)
    print("Total vowels:", result)

except TypeError as error:
    print(f"Error: {error}")
