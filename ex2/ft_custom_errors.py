class GardenError(Exception):
    """Exception Who check WaterError and PlantError"""
    pass


class WaterError(GardenError):
    """Exception Who check the water level"""
    pass


class PlantError(GardenError):
    """Exception Who check the state of the plant"""
    pass


def check_water(water_level):
    """Verify the water level and relieve the exception if is void"""
    if water_level == "void":
        raise WaterError("Not enough water in the tank!")
    return


def check_plant(plant_state):
    """Verify the plant state and relieve the exception if is wilting"""
    if plant_state == "wilting":
        raise PlantError("The plant is wilting!")
    return


def check_garden(plant_state, water_level):
    """Docstring for check_garden"""
    if plant_state == "wilting":
        raise PlantError("The plant is wilting!")
    if water_level == "void":
        raise WaterError("Not enough water in the tank!")
    return


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    try:
        check_plant("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water("void")
    except WaterError as e:
        print(f"Caught WaterError: {e} \n")

    print("Testing catching all garden errors...")

    try:
        check_plant("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water("void")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


ft_custom_errors()
