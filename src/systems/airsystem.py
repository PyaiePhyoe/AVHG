from system import System
from component import Component
from state_variable import State_Variable

class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        self.air_cleaner = AirCleaner()
        self.add_component(self.air_cleaner)

    def show_info(self):
        print(f"Name: {self.name}\nDescription: {self.description}\nHealth: {self.health}\nStatus: {self.status}")
        self.list_components()
        
class AirCleaner(Component):
    def __init__(self):
        super().__init__(name="Air Cleaner", description="Filter air")
        self.filter_quality = State_Variable(name="Filter Quality", description="Quality of Filter", unit="Quality", max_value="NA", min_value="NA", normal_max="NA", normal_min="NA", measurement="Quality of filter element", source="Component", timestamp="", value="Good")
        self.add_state_variable(self.filter_quality)

class MAF:
    def __init__(self):
        self.name = "MAF"
        self.maf = 5
        self.intakeAirTemp = 20

