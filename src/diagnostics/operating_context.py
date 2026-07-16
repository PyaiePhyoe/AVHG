from diagnostics.obd2 import dummy_data


class Operating_Context:
    def __init__(self):
        self.rpm = dummy_data["engine speed"]
        self.vehicle_speed = dummy_data["vehicle speed"]
        self.accelerator_pedal_position = dummy_data["accelerator position"]
        self.coolant_temp = dummy_data["coolant temp"]
        self.throttle_position = dummy_data["actual throttle position"]

    def engine_condition(self):
        if (
            self.vehicle_speed == 0
            and self.throttle_position == 0
            and self.accelerator_pedal_position <= 5
        ):
            if self.coolant_temp >= 80 and self.rpm <= 900 and self.rpm >= 650:
                return "Warm Idling"
            elif self.coolant_temp < 40 and self.rpm <= 1200 and self.rpm >= 650:
                return "Cold Starting"
        elif self.accelerator_pedal_position >= 10 and self.rpm >= 1200:
            return "Acceleration"
        elif (
            self.accelerator_pedal_position >= 10
            and self.accelerator_pedal_position <= 40
            and self.vehicle_speed >= 40
            and self.coolant_temp >= 80
        ):
            return "Cruise"
        if (
            self.rpm >= 900
            and self.accelerator_pedal_position == 0
            and self.vehicle_speed >= 0
            and self.throttle_position == 0
        ):
            return "Deceleration"
