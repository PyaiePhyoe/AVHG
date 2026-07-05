from component import Component

class Actuator (Component):
    def __init__(self, name, description,unit, max_value, min_value, normal_min, normal_max, activity):
        super().__init__(name, description)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value
        self.normal_max = normal_max
        self.normal_min = normal_min
        self.activity = activity
        self.command = None
        self.feedback = None
        self.enabled = True

    def set_command(self,value):
        self.command = value

    def get_feedback(self):
        return self.feedback
    
    def update_feedback(self, value):
        self.feedback = value

    def is_enabled(self):
        return self.enabled


    