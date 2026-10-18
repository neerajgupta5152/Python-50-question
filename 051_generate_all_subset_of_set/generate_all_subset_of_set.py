
def generate_subsets(numbers: list) -> list:
    """
    Generate all possible subsets of a list.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        list: A list containing all possible subsets.

    Raises:
        TypeError: If input is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    result = [[]]

    for num in numbers:
        for subset in result.copy():
            result.append(subset + [num])

    return result


def main():
    try:
        numbers = [1, 2, 3]
        result = generate_subsets(numbers)
        print(result)

    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
