from system import System





class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        

    def show_info(self):
        print(f"This is {self.name} with {self.description} and this has {self.health} health, {self.status} and {self.components}")
        
class AirCleaner:
    def __init__(self):
            self.name = "AirCleaner"


class MAF:
    def __init__(self):
        self.name = "MAF"
        self.maf = 5
        self.intakeAirTemp = 20

