from system import System
from component import Component
from variable_data import Variable_Data
import pandas as pd


class Engine:
    def __init__(self):
        self.name = "Toyota 1GD-FTV Digital Twin"
        self.health = 100
        self.status = "Normal"
        self.systems = {}
        self.manual_data = {}

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

        for index, (data, value) in enumerate(self.manual_data.items(), start=1):
            print(
                f"{index}. {value.name} | Range - between {value.min_value} and {value.max_value}"
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

    def read_manaul_data(self):
        file_path = "src/data/DataList_1GDFTV.xlsx"

        try:
            data = pd.read_excel(file_path)
            for index, row in data.iterrows():
                self.data_name = str(row["Tester Display"])
                self.measure = str(row["Measurement Item"])
                self.min_value = str(row["RangeMin"])
                self.max_value = str(row["RangeMax"])
                self.unit = str(row["Unit"])
                self.normal_min = str(row["NormalMin"])
                self.normal_max = str(row["NormalMax"])
                self.running_min = str(row["RunningMin"])
                self.running_max = str(row["RunningMax"])

                self.manual_data[self.data_name] = Variable_Data(
                    name=self.data_name,
                    description=self.measure,
                    unit=self.unit,
                    min_value=self.min_value,
                    max_value=self.max_value,
                    measurement=self.measure,
                    normal_min=self.normal_min,
                    normal_max=self.normal_max,
                    running_min=self.running_min,
                    running_max=self.running_max,
                )

        except FileNotFoundError:
            print(
                f"Error: Could not find the Excel file at {file_path}. Please check the file name."
            )
