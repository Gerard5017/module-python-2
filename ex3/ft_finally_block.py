def water_plants(plant_list):
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


def test_watering_system():
    valid_lst = ["Tomato", "Apple", "Monstera"]
    invalid_lst = ["Tomato", None, "Orchid"]
    print("Testing normal watering...\n")
    water_plants(valid_lst)
    print("Testing with error...\n")
    water_plants(invalid_lst)
    print("Cleanup always happens, even with errors!")


test_watering_system()
