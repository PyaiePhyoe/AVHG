from system import System
from component import Component

class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        self.air_cleaner = AirCleaner()
        self.add_component(self.air_cleaner)

    def show_info(self):
        print(f"This is {self.name} with {self.description} and this has {self.health} health, {self.status} status and components such as ", end="")
        self.list_components()
        

class AirCleaner(Component):
    def __init__(self):
        super().__init__(name="Air Cleaner", description="Filter air")
        


class MAF:
    def __init__(self):
        self.name = "MAF"
        self.maf = 5
        self.intakeAirTemp = 20

