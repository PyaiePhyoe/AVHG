from system import System
from component import Component
from sensor import Sensor
from diagnostics.diagnose_variable import Diagnose_Variable
from diagnostics.operating_context import Operating_Context


class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        # self.air_cleaner = AirCleaner()
        # self.add_component(self.air_cleaner)
        self.mass_airflow_meter = Mass_Airflow_Meter()
        self.add_component(self.mass_airflow_meter)

    def show_info(self):
        print(
            f"Name: {self.name}\nDescription: {self.description}\nHealth: {self.health}\nStatus: {self.status}\n"
        )
        self.list_components()

    def diagnose_system(self):
        self.engine_condition = Operating_Context().engine_condition()
        for sensor in self.components:
            for variable_name, variable_data in sensor.actual_data.items():
                self.test_result = Diagnose_Variable(
                    variable_name, variable_data, self.engine_condition
                )
                print(self.test_result.check())


class Mass_Airflow_Meter(Sensor):
    def __init__(self):
        super().__init__(
            name="Mass Airflow Meter",
            description="a sensor that measures air density and amount entering the engine.",
        )
        self.read_actual_maf = self.read_actual_data(name="MAF")
        self.read_actual_map = self.read_actual_data(name="MAP")


"""
class AirCleaner(Component):
    def __init__(self):
        super().__init__(name="Air Cleaner", description="Filter air")
        self.filter_quality = State_Variable(
            name="Filter Quality", 
            description="Quality of Filter", 
            unit="Quality", 
            max_value="NA", 
            min_value="NA", 
            normal_max="NA", 
            normal_min="NA", 
            measurement="Quality of filter element", 
            source="Component", 
            timestamp="", 
            value="Good")
        self.add_state_variable(self.filter_quality)
"""
