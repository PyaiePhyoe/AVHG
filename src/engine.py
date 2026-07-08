from systems.airsystem import AirSystem


class Engine:
    def __init__(self):
        self.name = "Toyota 1GD-FTV"
        self.systems = []

    def show_info(self):
        print(f"Engine: {self.name}\n")
        """
        for i in self.systems:
            print(f"{i.name} - {i.description}")
            for component in i.components:
                print(component.name)
                if component.actual_data:
                    for name, data in component.actual_data.items():
                        print(f"{name} - {data}")
                else:
                    pass
        """

    def start(self):
        self.air_system = AirSystem()
        self.systems.append(self.air_system)
