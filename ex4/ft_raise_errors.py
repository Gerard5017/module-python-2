def check_plant_health(plant_name, water_level, sunlight_hours):
    if (not plant_name or plant_name == ""):
        raise ValueError("Plant name cannot be empty!")
    if (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low min 1")
    if (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high max 10")
    if (sunlight_hours < 2):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low min 2")
    if (sunlight_hours > 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high max 12")
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
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


test_plant_checks()
