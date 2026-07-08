from system import System
from component import Component
from sensor import Sensor
from diagnostics.operating_context import Operating_Context
from diagnostics.diagnose_variable import Diagnose_Variable


class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        # self.air_cleaner = AirCleaner()
        # self.add_component(self.air_cleaner)
        self.mass_airflow_meter = Mass_Airflow_Meter()
        self.add_component(self.mass_airflow_meter)

    def diagnose_system(self):
        print(f"System Name: {self.name}\nDescription: {self.description}")
        print("---------------\n")
        self.engine_condition = Operating_Context().engine_condition()
        print(f"Components of {self.name}")
        print("---------------\n")
        for component in self.components:
            print(f"Component Name: {component.name} - {component.description}")
            for variable_name, variable_data in component.actual_data.items():
                self.test_result = Diagnose_Variable(
                    variable_name, variable_data, self.engine_condition
                )
                print(self.test_result.check())

                # print(self.test_result.check_result[variable_name]["Status"])
                if component.health == 100.00 and component.status == "Normal":
                    if (
                        self.test_result.check_result[variable_name]["Status"]
                        != "Normal"
                    ):
                        component.health = 0
                        component.status = "Abnormal"
                    else:
                        pass
                else:
                    pass

            print(
                f"Component Condition -> Health: {component.health} | Status: {component.status}"
            )
            if self.health == 100.00 and self.status == "Normal":
                if component.health == 0 or component.status == "Abnormal":
                    self.health = 0
                    self.status = "Abnormal"
                else:
                    pass
            else:
                pass
        print(f"System Condition -> Health: {self.health} | Status: {self.status}")
        print("---------------\n")


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
