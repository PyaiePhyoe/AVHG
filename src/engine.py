from systems.airsystem import AirSystem


class Engine:
    def __init__(self):
        self.name = "Toyota 1GD-FTV Digital Twin"
        self.health = 100
        self.status = "Normal"
        self.systems = []

    def show_info(self):
        print(f"Engine: {self.name}\n")

    def start(self):
        self.air_system = AirSystem()
        self.systems.append(self.air_system)
