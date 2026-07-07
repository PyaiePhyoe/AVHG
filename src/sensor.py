from component import Component
from diagnostics.obd2 import obd2_data


class Sensor(Component):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100.00
        self.status = "Normal"
        self.actual_data = {}

    def read_actual_data(self, name):
        self.actual_data.update({name: obd2_data[name]})
