def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate plant health parameters and ensure they're within range.

    Checks that the plant name is valid and that water level and
    sunlight hours fall within acceptable ranges for plant health.

    :param plant_name: Name of the plant to check
    :type plant_name: str or None
    :param water_level: Water level (must be between 1 and 10)
    :type water_level: int
    :param sunlight_hours: Daily sunlight hours (must be between 2 and 12)
    :type sunlight_hours: int
    :raises ValueError: If plant_name is empty or None
    :raises ValueError: If water_level is less than 1 or greater than 10
    :raises ValueError: If sunlight_hours is less than 2 or greater than 12
    :return: Success message if all parameters are valid
    :rtype: str
    """
    if not plant_name or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low min 1")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high max 10")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low min 2")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high max 12"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test the plant health checker with various valid and invalid inputs.

    Demonstrates how the check_plant_health function validates parameters
    and raises exceptions for invalid inputs. All exceptions are caught
    and handled gracefully.

    :return: None (prints test results to console)
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        print(check_plant_health("Orchid", 6, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(None, 6, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("Orchid", 13, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("Orchid", 6, 1))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
