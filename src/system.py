from entity import Entity
from component import Component


class System(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.components = []

    def add_component(self, component_list):
        for component in component_list:
            if not isinstance(component, Component):
                raise TypeError(f"{component} is not a component.")
            self.components.append(component)
