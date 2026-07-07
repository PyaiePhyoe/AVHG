from diagnostics.obd2 import obd2_data


class Operating_Context:
    def __init__(self):
        self.rpm = obd2_data["RPM"]
        self.vehicle_speed = obd2_data["Vehicle Speed"]
        self.accelerator_pedal_position = obd2_data["Accelerator Pedal Position"]
        self.coolant_temp = obd2_data["Coolant Temperature"]
        self.throttle_position = obd2_data["Throttle Position"]

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
