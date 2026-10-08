# Power function without using ** operator or pow()
def my_power(x: int, y: int) -> int:
    """
    Calculate x raised to power y using for loop.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Input must be an integer")
    if y < 0:
        raise ValueError("Power must be positive")

    result = 1
    for i in range(y):
        result = result * x
    return result

# Main execution
if __name__ == "__main__":
    while True:
        try:
            x = int(input("Enter the base value: "))
            y = int(input("Enter the power value: "))
            print(f"Result: {x}^{y} = {my_power(x, y)}")
            break
        except ValueError as e:
            if "invalid literal" in str(e):
                print("TypeError: Enter input must be integer")
            else:
                print(f"ValueError: {e}")
        except TypeError as e:
            print(f"TypeError: {e}")
        except Exception as e:
            print(f"Error: {e}")
