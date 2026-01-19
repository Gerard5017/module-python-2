def garden_operations(error_type):
    """
    Generate Different Error

    :param error_type: Choose the type of the error (value, zero, file, key)
    """
    if (error_type == "value"):
        n = int("abc")
        n + 3
    elif (error_type == "zero"):
        n = 9 / 0
    elif (error_type == "file"):
        open("missing.txt")
    elif (error_type == "key"):
        plant = {"Bamboo": 5}
        plant["missing"]


def test_error_types():
    """
    Test the funtion garden_operations with different Error
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


test_error_types()
