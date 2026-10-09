
def prime_number(number: int) -> bool:
    """
    Find whether a number is prime or not.
    """
    # Exception handling
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Input must be an integer")

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    try:
        for number in range(100, 201):
            if prime_number(number):
                print(number)

    except (TypeError, ValueError) as error:
        print(f"Error: Invalid input. {error}")
