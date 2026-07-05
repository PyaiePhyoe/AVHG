from component import Component
from state_variable import State_Variable

class Sensor(Component):
    def __init__(self, name, description):
        super().__init__(name, description)
        
        self.state_variables = []
    
    def add_state_variable(self, variable):
        if not isinstance(variable, State_Variable):
            raise TypeError(
                f"{variable} is not a variable."
            )
        self.state_variables.append(variable)

    def read(self):
        return self.state_variables
    
    

