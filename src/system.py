from entity import Entity
from component import Component

class System(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.components = []

    def add_component(self,component):
        if not isinstance(component, Component):
            raise TypeError(
                f"{component} is not a component."
            )
        self.components.append(component)

    def list_components(self):
        for component in self.components:
            if len(self.components) == 1: 
                return print(f"{component.name}.")

            if self.components.index(component) == len(self.components) - 1: 
                return print(f"and {component.name}.")
            return print(f"{component.name},")
        
    def get_component(self, name):
        for component in self.components:
            if component.name == name:
                return component
        return None