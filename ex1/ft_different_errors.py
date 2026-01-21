def garden_operations(error_type):
    """
    Generate different types of errors for demonstration purposes.

    This function intentionally raises different exceptions based on
    the error_type parameter to demonstrate exception handling.

    :param error_type: Type of error to generate
                      ('value', 'zero', 'file', 'key')
    :type error_type: str
    :raises ValueError: When error_type is 'value'
    :raises ZeroDivisionError: When error_type is 'zero'
    :raises FileNotFoundError: When error_type is 'file'
    :raises KeyError: When error_type is 'key'
    :return: None
    """
    if error_type == "value":
        n = int("abc")
        n + 3
    elif error_type == "zero":
        n = 9 / 0
    elif error_type == "file":
        open("missing.txt")
    elif error_type == "key":
        plant = {"Bamboo": 5}
        plant["missing"]


def test_error_types():
    """
    Test the garden_operations function with different error types.

    Demonstrates how to catch and handle multiple types of exceptions
    using try-except blocks. Shows that the program continues running
    even after exceptions are caught.

    :return: None (prints test results to console)
    """
    print("=== Garden Error Types Demo ===")
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing/plant'")

    print("Testing multiple errors together...")
    try:
        garden_operations("key")
        garden_operations("zero")
    except (KeyError, ZeroDivisionError):
        print("Caught an Error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
