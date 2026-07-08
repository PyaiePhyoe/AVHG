from diagnostics.operating_context import Operating_Context
from diagnostics.diagnose_variable import Diagnose_Variable


class Diagnose:
    def __init__(self, entity):
        self.entity = entity

    def start(self):
        for system in self.entity.systems:
            print(f"System Name: {system.name}\nDescription: {system.description}")
            print("---------------\n")
            self.engine_condition = Operating_Context().engine_condition()
            print(f"Components of {system.name}")
            print("---------------\n")
            for index, component in enumerate(system.components, start=1):
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
                if system.health == 100.00 and system.status == "Normal":
                    if component.health == 0 or component.status == "Abnormal":
                        system.health = 0
                        system.status = "Abnormal"
                    else:
                        pass
                else:
                    pass
            print(
                f"System Condition -> Health: {system.health} | Status: {system.status}"
            )
            print("---------------\n")
