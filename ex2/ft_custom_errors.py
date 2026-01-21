class GardenError(Exception):
    """
    Base exception class for garden-related errors.

    This serves as the parent class for all garden-specific exceptions,
    allowing for catching all garden errors with a single except clause.
    """

    pass


class WaterError(GardenError):
    """
    Exception raised for water-related issues.

    This exception is raised when there are problems with water levels
    or water availability in the garden system.
    """

    pass


class PlantError(GardenError):
    """
    Exception raised for plant health issues.

    This exception is raised when a plant is in poor condition
    or experiencing health problems.
    """

    pass


def check_water(water_level: str) -> None:
    """
    Verify the water level in the tank.

    Checks if there is sufficient water available and raises an
    exception if the tank is empty.

    :param water_level: Current water level status
    :type water_level: str
    :raises WaterError: If water level is 'void'
    :return: None
    """
    if water_level == "void":
        raise WaterError("Not enough water in the tank!")
    return


def check_plant(plant_state: str) -> None:
    """
    Verify the plant's health state.

    Checks the condition of a plant and raises an exception
    if the plant is wilting or unhealthy.

    :param plant_state: Current state of the plant
    :type plant_state: str
    :raises PlantError: If plant state is 'wilting'
    :return: None
    """
    if plant_state == "wilting":
        raise PlantError("The plant is wilting!")
    return


def check_garden(plant_state: str, water_level: str) -> None:
    """
    Perform comprehensive checks on garden conditions.

    Verifies both plant health and water availability,
    raising appropriate exceptions for any issues found.

    :param plant_state: Current state of the plant
    :type plant_state: str
    :param water_level: Current water level status
    :type water_level: str
    :raises PlantError: If plant state is 'wilting'
    :raises WaterError: If water level is 'void'
    :return: None
    """
    if plant_state == "wilting":
        raise PlantError("The plant is wilting!")
    if water_level == "void":
        raise WaterError("Not enough water in the tank!")
    return


def ft_custom_errors() -> None:
    """
    Demonstrate custom exception handling for garden errors.

    Tests all custom exception types and shows how they can be
    caught individually or as a group using the base GardenError class.

    :return: None (prints test results to console)
    """
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


if __name__ == "__main__":
    ft_custom_errors()
