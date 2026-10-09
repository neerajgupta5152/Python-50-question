
def prime_number(number: int) -> bool:
    """
    Check whether a number is prime or not.
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


def main():
    """Take input from the user and display the result."""

    while True:
        try:
            number = int(input("Enter the number: "))

            if prime_number(number):
                print(number, "is a prime number")
            else:
                print(number, "is not a prime number")

            break

        except (TypeError, ValueError) as error:
            print(f"Error: Invalid input. {error}")


if __name__ == "__main__":
    main()
