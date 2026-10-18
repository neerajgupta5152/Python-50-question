
def check_subsequence(larger_list: list, smaller_list: list) -> bool:
    """
    Check whether smaller_list is a subsequence of larger_list.

    Args:
        larger_list (list): The original list.
        smaller_list (list): The list to search for.

    Returns:
        bool: True if a subsequence exists, otherwise False.

    Raises:
        TypeError: If inputs are not lists.
    """
    # Validate input types
    if not isinstance(larger_list, list) or not isinstance(smaller_list, list):
        raise TypeError("Both inputs must be lists.")

    i = 0

    # Check elements in the same order
    for num in larger_list:
        if i < len(smaller_list) and num == smaller_list[i]:
            i += 1

    return i == len(smaller_list)


def main():
    try:
        larger_list = [1, 3, 5, 7, 9]
        smaller_list = [3, 7]
        print(check_subsequence(larger_list, smaller_list))

        larger_list = [1, 3, 5, 7, 9]
        smaller_list = [3, 8]
        print(check_subsequence(larger_list, smaller_list))

    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
