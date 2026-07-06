from component import Component
from state_variable import State_Variable

class Sensor(Component):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.state_variables = []
    

    
    

