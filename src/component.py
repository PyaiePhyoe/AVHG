from entity import Entity
from state_variable import State_Variable

class Component(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.state_variables = []

    def add_state_variable(self, variable):
        if not isinstance(variable, State_Variable):
            raise TypeError(
                f"{variable} is not a variable."
            )
        self.state_variables.append(variable)

    def list_state_variables(self):
        for state_variable in self.state_variables:
            state_variable.read_variable()