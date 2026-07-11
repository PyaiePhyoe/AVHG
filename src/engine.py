from system import System
from component import Component
import pandas as pd


class Engine:
    def __init__(self):
        self.name = "Toyota 1GD-FTV Digital Twin"
        self.health = 100
        self.status = "Normal"
        self.systems = {}

    def show_info(self):
        print(f"Engine: {self.name}\n")
        # print(self.systems)
        # print(f"{self.systems['AIR'].name}\n{self.systems['AIR'].components}")

        for index, (system, obj) in enumerate(self.systems.items(), start=1):
            print(
                f"{index} - {obj.name} | {obj.description} | {obj.health} | {obj.status}\n"
            )
            for index, (component, value) in enumerate(obj.components.items(), start=1):
                print(
                    f"------>{index} - {value.name} | {value.description} | {value.health} | {value.status}\n"
                )

    def start(self):

        file_path = "src/data/Engine.xlsx"

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                if str(row["System Name"]) not in self.systems:
                    self.system_name = str(row["System Name"])
                    self.system_description = str(row["Description"])

                    self.systems[self.system_name] = System(
                        name=self.system_name, description=self.system_description
                    )

                else:
                    pass
                self.system = self.systems[str(row["System Name"])]
                if str(row["ComponentName"]) not in self.system.components:
                    self.component_name = str(row["ComponentName"])
                    self.component_description = str(row["Description"])
                    self.system.components[self.component_name] = Component(
                        name=self.component_name,
                        description=self.component_description,
                    )

        except FileNotFoundError:
            print(
                f"Error: Could not find the Excel file at {file_path}. Please check the file name."
            )
