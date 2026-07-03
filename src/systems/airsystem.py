class AirSystem:
    def __init__(self):
        self.name = "AirSystem"
        self.air_cleaner = AirCleaner()
        self.MAF = MAF()

    def show_info(self):
        print(f"{self.name} has {self.air_cleaner.name} and {self.MAF.name}")
        
class AirCleaner:
    def __init__(self):
            self.name = "AirCleaner"


class MAF:
    def __init__(self):
        self.name = "MAF"
        self.maf = 5
        self.intakeAirTemp = 20

