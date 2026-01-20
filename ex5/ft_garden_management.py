class GardenError(Exception):
    """Personalized exception for garden errors"""
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 100

    def add_plant(self, name, water_level, sunlight_hours):
        if not name or name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1 or water_level > 10:
            raise ValueError("Water level must be between 1 and 10")
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError("Sunlight hours must be between 2 and 12")
        self.plants[name] = {"water": water_level, "sun": sunlight_hours}
        print(f"Added {name} successfully")

    def water_plants(self):
        try:
            print("Opening watering system")
            for name in self.plants:
                if self.water_tank < 10:
                    raise GardenError("Not enough water in tank")
                print(f"Watering {name} - success")
                self.water_tank -= 10
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self, plant_name):
        if plant_name not in self.plants:
            raise GardenError(f"Plant '{plant_name}' not found in garden")
        plant = self.plants[plant_name]
        water = plant["water"]
        sun = plant["sun"]
        if (not plant_name or plant_name == ""):
            raise ValueError("Plant name cannot be empty!")
        if (water < 1):
            raise ValueError(f"Water level {water} is too low min 1")
        if (water > 10):
            raise ValueError(f"Water level {water} is too high max 10")
        if (sun < 2):
            raise ValueError(f"Sunlight hours {sun} is too low min 2")
        if (sun > 12):
            raise ValueError(f"Sunlight hours {sun} is too high max 12")
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
    

def test_garden_management():
    print("=== Garden Management System ===")
    garden = GardenManager()
    print("\nAdding plants to garden...")

    try:
        garden.add_plant("tomato", 5, 8)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    
    try:
        garden.add_plant("lettuce", 6, 6)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    
    try:
        garden.add_plant("", 5, 8)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    
    print("\nWatering plants...")
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Error watering: {e}")
    
    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
    except (ValueError, GardenError) as e:
        print(f"Error checking tomato: {e}")
    
    garden.plants["lettuce"]["water"] = 15
    try:
        garden.check_plant_health("lettuce")
    except ValueError as e:
        print(f"Error checking lettuce: {e}")
    
    print("\nTesting error recovery...")
    garden.water_tank = 5
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")


test_garden_management()