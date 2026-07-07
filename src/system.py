from entity import Entity
from component import Component


class System(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.components = []

    def add_component(self, component):
        if not isinstance(component, Component):
            raise TypeError(f"{component} is not a component.")
        self.components.append(component)

    def list_components(self):
        print(f"Components of {self.name}")
        print("---------------\n")
        for component in self.components:
            print(
                f"{component.name} | Health: {component.health} | Status: {component.status}\n"
            )
            for name, data in component.actual_data.items():
                print(f"{name}: {data}")
            print("---------------")

    def get_component(self, name):
        for component in self.components:
            if component.name == name:
                return component
        return None
