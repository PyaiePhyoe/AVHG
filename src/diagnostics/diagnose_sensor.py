from operating_context import Operating_Context


class Diagnose_Sensor:
    def __init__(self, component):
        self.component = component
        self.engine_condition = Operating_Context().engine_condition()
