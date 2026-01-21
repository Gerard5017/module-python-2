def water_plants(plant_list: list) -> None:
    """
    Water a list of plants with proper resource cleanup.

    Simulates opening a watering system, watering each plant,
    and ensuring the system is properly closed even if errors occur.

    :param plant_list: List of plant names to water
    :type plant_list: list
    :raises ValueError: If an invalid plant (None) is encountered
    :return: None (prints watering status to console)
    """
    try:
        print("Opening watering system")
        for i in plant_list:
            if i is None:
                raise ValueError(f"Cannot water {i} - invalid plant!")
            print(f"watering {i}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    """
    Test the watering system with valid and invalid plant lists.

    Demonstrates that the finally block executes in both success
    and error scenarios, ensuring proper resource cleanup.

    :return: None (prints test results to console)
    """
    valid_lst = ["Tomato", "Apple", "Monstera"]
    invalid_lst = ["Tomato", None, "Orchid"]

    print("Testing normal watering...\n")
    water_plants(valid_lst)

    print("Testing with error...\n")
    water_plants(invalid_lst)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
