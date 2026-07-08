from system import System
from component import Component
from sensor import Sensor
from diagnostics.operating_context import Operating_Context
from diagnostics.diagnose_variable import Diagnose_Variable


class AirSystem(System):
    def __init__(self):
        super().__init__(name="AirSystem", description="Intake air for the engine.")
        self.air_cleaner = AirCleaner()
        self.mass_airflow_meter = Mass_Airflow_Meter()
        self.component_list = [self.air_cleaner, self.mass_airflow_meter]
        self.add_component(self.component_list)

    def diagnose_system(self):
        print(f"System Name: {self.name}\nDescription: {self.description}")
        print("---------------\n")
        self.engine_condition = Operating_Context().engine_condition()
        print(f"Components of {self.name}")
        print("---------------\n")
        for index, component in enumerate(self.components, start=1):
            print(f"{index}. {component.name} - {component.description}")
            if component.actual_data:
                for variable_name, variable_data in component.actual_data.items():
                    self.test_result = Diagnose_Variable(
                        variable_name, variable_data, self.engine_condition
                    )
                    print(self.test_result.check())

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
            else:
                print(f"Check {component.name} physically.")
            print(
                f"Component Condition -> Health: {component.health} | Status: {component.status}"
            )
            print("---------------\n")
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


class AirCleaner(Component):
    def __init__(self):
        super().__init__(name="Air Clearner", description="Filter the intake air.")
