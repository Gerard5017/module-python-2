def check_temperature(temp_str):
    """
    Check if the temperature is suitable for plants.

    Validates that the temperature is within the acceptable range
    (0°C to 40°C) for plant growth. Handles invalid input gracefully.

    :param temp_str: The ambient temperature as a string
    :type temp_str: str
    :return: None (prints result to console)
    """
    try:
        t = int(temp_str)
        if t > 40:
            print(f"Error: {t}°C is too hot for plants (max 40°C)")
        elif t < 0:
            print(f"Error: {t}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {t}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Test the check_temperature function with various inputs.

    Tests the function with valid temperatures, invalid formats,
    and out-of-range values to demonstrate error handling.

    :return: None (prints test results to console)
    """
    t1 = "25"
    t2 = "abc"
    t3 = "100"
    t4 = "-50"
    print("=== Garden Temperature Checker ===")
    print(f"Testing temperature: {t1}")
    check_temperature(t1)
    print(f"Testing temperature: {t2}")
    check_temperature(t2)
    print(f"Testing temperature: {t3}")
    check_temperature(t3)
    print(f"Testing temperature: {t4}")
    check_temperature(t4)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
