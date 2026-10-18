
def reverse_array(numbers: list) -> None:
    """
    Reverse the original list without creating a new list.

    Args:
        numbers (list): The list to reverse.

    Returns:
        None: Modifies the original list in place.

    Raises:
        TypeError: If input is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1


def main():
    try:
        numbers = [1, 2, 3, 4, 5]

        reverse_array(numbers)

        print(numbers)

    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
