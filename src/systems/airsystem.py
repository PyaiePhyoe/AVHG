from system import System
from component import Component
from sensor import Sensor


class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        self.air_cleaner = AirCleaner()
        self.mass_airflow_meter = Mass_Airflow_Meter()
        self.accel_sensor = Accelerator_Pedal_Sensor()
        self.component_list = [
            self.air_cleaner,
            self.mass_airflow_meter,
            self.accel_sensor,
        ]
        self.add_component(self.component_list)


class Mass_Airflow_Meter(Sensor):
    def __init__(self):
        super().__init__(
            name="Mass Airflow Meter",
            description="a sensor that measures air density and amount entering the engine.",
        )
        self.read_actual_maf = self.read_actual_data(name="MAF")
        self.read_actual_map = self.read_actual_data(name="MAP")


class AirCleaner(Component):
    def __init__(self):
        super().__init__(name="Air Clearner", description="Filter the intake air.")


class Accelerator_Pedal_Sensor(Sensor):
    def __init__(self):
        super().__init__(
            name="Accelerator Pedal Position Sensor",
            description="Detects the position of the accelerator pedal position.",
        )
        self.read_actual_accel = self.read_actual_data(
            name="Accelerator Pedal Position"
        )
