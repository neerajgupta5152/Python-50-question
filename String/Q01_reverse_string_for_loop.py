# Reverse the string using for loop - without slicing
def reverse_string(my_string: str) -> str:
    """
    Reverse a string using for loop without using slicing [::-1].
    """
    if not isinstance(my_string, str):
        raise TypeError("Input must be a string")
    if not my_string.strip():
        raise ValueError("String cannot be empty")

    reverse = ""
    for char in my_string:
        reverse = char + reverse
    return reverse

# Main execution
if __name__ == "__main__":
    while True:
        try:
            my_string = input("Enter the string: ")
            result = reverse_string(my_string)
            print(f"Reversed string: {result}")
            break
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
