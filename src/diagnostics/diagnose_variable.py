from diagnostics.core.database import database


class Diagnose_Variable:
    def __init__(self, variable_name, variable_data, engine_condition):
        self.variable_name = variable_name
        self.variable_data = variable_data
        self.engine_condition = engine_condition
        self.min_value = database[self.variable_name]["min_value"]
        self.max_value = database[self.variable_name]["max_value"]
        self.expected_min_value = database[self.variable_name][engine_condition][
            "normal_min"
        ]
        self.expected_max_value = database[self.variable_name][engine_condition][
            "normal_max"
        ]
        self.check_result = {
            self.variable_name: {
                "Variable Data": self.variable_data,
                "Status": "Normal",
            }
        }

    def check(self):
        if self.variable_data > self.min_value and self.variable_data < self.max_value:
            if (
                self.variable_data >= self.expected_min_value
                and self.variable_data <= self.expected_max_value
            ):
                return f"{self.variable_name} \n Measured Value: {self.variable_data}\n Expected Value: Between {self.expected_min_value} and {self.expected_max_value}\n Status: {self.check_result[self.variable_name]['Status']}"
            else:
                self.check_result[self.variable_name]["Status"] = "Abnormal"
                return f"{self.variable_name} \n Measured Value: {self.variable_data}\n Expected Value: Between {self.expected_min_value} and {self.expected_max_value}\n Status: {self.check_result[self.variable_name]['Status']}"
        else:
            self.check_result[self.variable_name]["Status"] = "Invalid"
            return f"{self.variable_name} \n Measured Value: {self.variable_data}\n Expected Value: Between {self.expected_min_value} and {self.expected_max_value}\n Status: {self.check_result[self.variable_name]['Status']}"
