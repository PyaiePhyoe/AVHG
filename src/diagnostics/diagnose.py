from diagnostics.operating_context import Operating_Context
from diagnostics.diagnose_variable import Diagnose_Variable


class Diagnose:
    def __init__(self, entity):
        self.entity = entity

    def start(self):
        self.engine_operating_condition = Operating_Context().engine_condition()
        print(
            f"Current Engine Operation\n{self.engine_operating_condition}\n----------------\n"
        )
        print("Systems")
        print("---------------\n")
        self.engine_health = []
        for system in self.entity.systems:
            print(f"System Name: {system.name}\nDescription: {system.description}")
            print("---------------\n")
            print(f"Components of {system.name}")
            print("---------------\n")
            self.system_health = []
            for index, component in enumerate(system.components, start=1):
                print(f"{index}. {component.name} - {component.description}")

                if component.actual_data:
                    self.variable_health = []
                    for variable_name, variable_data in component.actual_data.items():
                        self.test_result = Diagnose_Variable(
                            variable_name,
                            variable_data,
                            self.engine_operating_condition,
                        )
                        print(self.test_result.check())
                        if (
                            self.test_result.check_result[variable_name]["Status"]
                            != "Normal"
                        ):
                            if (
                                self.test_result.check_result[variable_name]["Status"]
                                == "Abnormal"
                            ):
                                self.variable_health.append(70)
                            else:
                                self.variable_health.append(0)
                        else:
                            self.variable_health.append(100)

                    self.component_score = sum(self.variable_health) / len(
                        self.variable_health
                    )

                    component.health = self.component_score
                    if component.health < 100 and component.health > 30:
                        component.status = "Warning"
                    elif component.health <= 30 and component.health > 0:
                        component.status = "Abnormal"
                    elif component.health == 0:
                        component.status = "Invalid"
                else:
                    print(f"Check {component.name} physically.")
                print(
                    f"Component Condition -> Health: {component.health} | Status: {component.status}"
                )
                print("---------------\n")

                if component.status != "Normal":
                    if component.status == "Warning":
                        self.system_health.append(70)
                    elif component.status == "Abnormal":
                        self.system_health.append(30)
                    else:
                        self.system_health.append(0)
                else:
                    self.system_health.append(100)
            self.system_score = sum(self.system_health) / len(self.system_health)
            system.health = self.system_score
            if system.health < 100:
                system.status = "Warning"
            elif system.health <= 30 and system.health > 0:
                system.status = "Abnormal"
            elif system.health == 0:
                system.status = "Invalid"
            print(
                f"System Condition -> Health: {system.health} | Status: {system.status}"
            )
            print("---------------\n")
            if system.status != "Normal":
                if system.status == "Warning":
                    self.engine_health.append(70)
                elif system.status == "Abnormal":
                    self.engine_health.append(30)
                else:
                    self.engine_health.append(0)
            else:
                self.engine_health.append(100)
        self.engine_score = sum(self.engine_health) / len(self.engine_health)
        self.health = self.engine_score
        if self.health < 100 and system.health > 30:
            self.status = "Warning"
        elif self.health <= 30 and self.health > 0:
            self.status = "Abnormal"
        elif self.health == 0:
            self.status = "Invalid"
        print(f"Engine Condition -> Health: {self.health} | Status: {self.status}")
        print("---------------\n")
