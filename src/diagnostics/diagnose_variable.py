from diagnostics.core.database import database


class Diagnose_Variable:
    def __init__(self, variable_name, variable_data, engine_condition):
        self.variable_name = variable_name
        self.variable_data = variable_data
        self.engine_condition = engine_condition
        self.min_value = database[self.variable_name]["min_value"]
        self.max_value = database[self.variable_name]["max_value"]

    def check(self):

        if self.variable_data > self.min_value and self.variable_data < self.max_value:
            return f"{self.variable_name}: Valid"
        else:
            return f"{self.variable_name}: Invalid"
