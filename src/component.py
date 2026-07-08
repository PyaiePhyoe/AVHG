from entity import Entity


class Component(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.actual_data = None
