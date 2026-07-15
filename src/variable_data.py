from entity import Entity


class Variable_Data(Entity):
    def __init__(
        self,
        name,
        description,
        unit,
        max_value,
        min_value,
        normal_min,
        normal_max,
        running_min,
        running_max,
        measurement,
    ):
        super().__init__(name, description)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value
        self.normal_max = normal_max
        self.normal_min = normal_min
        self.measurement = measurement
        self.running_max = running_max
        self.running_min = running_min
