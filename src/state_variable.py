from entity import Entity

class State_Variable(Entity):
    def __init__(self, name, description, unit, max_value, min_value, normal_max, normal_min, measurement, source, timestamp, value):
        super().__init__(name, description)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value
        self.normal_max = normal_max
        self.normal_min = normal_min
        self.measurement = measurement
        self.source = source
        self.timestamp = timestamp
        self.value = value

    def update(self, value):
        self.value = value

    def is_Valid (self):
        if self.value is None:
            return False
        if self.min_value is not None and self.value < self.min_value:
            return False
        if self.max_value is not None and self.value > self.max_value:
            return False
        return True
    
    def is_Normal (self):
        if self.value is None:
            return False
        if self.normal_min is not None and self.value < self.normal_min:
            return False
        if self.normal_max is not None and self.value > self.normal_max:
            return False
        return True