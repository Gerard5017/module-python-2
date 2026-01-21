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


class GardenManager():
    """
    A comprehensive garden management system.

    This class manages plants in a garden, tracking their water and
    sunlight requirements, managing a water tank, and providing
    functionality to add plants, water them, and check their health.

    :ivar plants: Dictionary storing plant information
    :type plants: dict
    :ivar water_tank: Current water level in the tank
    :type water_tank: int
    """

    def __init__(self) -> None:
        """
        Initialize a new GardenManager instance.

        Sets up an empty plant dictionary and initializes
        the water tank to 100 units.
        """
        self.plants = {}
        self.water_tank = 100

    def add_plant(self, name: str, water_level: int,
                  sunlight_hours: int) -> None:
        """
        Add a new plant to the garden with validation.

        Validates plant parameters and adds the plant to the garden
        if all values are within acceptable ranges.

        :param name: Name of the plant
        :type name: str
        :param water_level: Required water level (1-10)
        :type water_level: int or float
        :param sunlight_hours: Required daily sunlight (2-12 hours)
        :type sunlight_hours: int or float
        :raises ValueError: If name is empty
        :raises ValueError: If water_level is not between 1 and 10
        :raises ValueError: If sunlight_hours is not between 2 and 12
        :return: None (prints success message)
        """
        if not name or name == "":
            raise GardenError("Plant name cannot be empty!")
        if water_level < 1 or water_level > 10:
            raise WaterError("Water level must be between 1 and 10")
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise PlantError("Sunlight hours must be between 2 and 12")
        self.plants[name] = {"water": water_level, "sun": sunlight_hours}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Water all plants in the garden with proper resource management.

        Attempts to water each plant, checking if sufficient water
        is available in the tank. Uses a finally block to ensure
        the watering system is properly closed.

        :raises GardenError: If water tank has less than 10 units
        :return: None (prints watering status)
        """
        try:
            print("Opening watering system")
            for name in self.plants:
                if self.water_tank < 10:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {name} - success")
                self.water_tank -= 10
        except GardenError as e:
            print(f"Caught WaterError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        """
        Check the health status of a specific plant.

        Validates that the plant exists and that its water and
        sunlight parameters are within healthy ranges.

        :param plant_name: Name of the plant to check
        :type plant_name: str
        :raises GardenError: If plant is not found in the garden
        :raises ValueError: If plant_name is empty
        :raises ValueError: If water level is not between 1 and 10
        :raises ValueError: If sunlight hours is not between 2 and 12
        :return: None (prints health status)
        """
        if plant_name not in self.plants:
            raise GardenError(f"Plant '{plant_name}' not found in garden")

        plant = self.plants[plant_name]
        water = plant["water"]
        sun = plant["sun"]

        if not plant_name or plant_name == "":
            raise GardenError("Plant name cannot be empty!")
        if water < 1 or water > 10:
            raise WaterError(f"Water level {water} must be between 1 and 10")
        if sun < 2 or sun > 12:
            raise PlantError(f"Sunlight hours {sun} must be between 2 and 12")

        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """
    Test the complete garden management system.

    Demonstrates all features of the GardenManager class including:
    - Adding plants with validation
    - Watering plants with resource management
    - Checking plant health
    - Error handling and recovery

    :return: None (prints test results to console)
    """
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("lettuce", 6, 6)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Error watering: {e}")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
    except GardenError as e:
        print(f"Error checking tomato: {e}")

    garden.plants["lettuce"]["water"] = 15
    try:
        garden.check_plant_health("lettuce")
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    garden.water_tank = 15
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
