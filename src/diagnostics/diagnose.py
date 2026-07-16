from diagnostics.operating_context import Operating_Context
from diagnostics import obd2
import math


class Diagnose:
    def __init__(self, entity):
        self.entity = entity

    def start(self):
        self.engine_operating_condition = Operating_Context().engine_condition()
        print(
            f"Current Engine Operation\n{self.engine_operating_condition}\n----------------\n"
        )

        self.engine_health = []
        for index, (data, value) in enumerate(self.entity.manual_data.items(), start=1):
            print(
                f"{index}. {value.name} | Range - between {value.min_value} and {value.max_value} | Normal - between {value.normal_min} and {value.normal_max}",
            )
            if value.name.lower() in obd2.dummy_data:
                self.actual_data = obd2.dummy_data[value.name.lower()]
                print(f"Actual - {self.actual_data}")

                if str(value.min_value) not in (
                    "nan",
                    "On",
                    "Off",
                ) and str(value.max_value) not in ("nan", "On", "Off"):
                    if self.actual_data >= float(
                        value.min_value
                    ) and self.actual_data <= float(value.max_value):
                        print("Valid!")
                        if (
                            self.engine_operating_condition == "Warm Idling"
                            or self.engine_operating_condition == "Cold Starting"
                        ):
                            if str(value.normal_min) not in (
                                "nan",
                                "On",
                                "Off",
                            ) and str(value.normal_max) not in ("nan", "On", "Off"):
                                if self.actual_data >= float(
                                    value.normal_min
                                ) and self.actual_data <= float(value.normal_max):
                                    print("Normal!")
                                else:
                                    print("Abnormal!")
                            else:
                                print("Check visually!")
                        else:
                            if value.running_min not in (
                                "NA",
                                "On",
                                "Off",
                            ) and value.running_max not in ("NA", "On", "Off"):
                                if self.actual_data >= float(
                                    value.running_min
                                ) and self.actual_data <= float(value.running_max):
                                    print("Normal!")
                                else:
                                    print("Abnormal!")
                            else:
                                print("Check visually!")
                    else:
                        print("Invalid!")
                else:
                    print("Check visually!")
            else:
                pass
