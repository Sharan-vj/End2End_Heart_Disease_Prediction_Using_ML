# Import Dependencies
import os
import pandas as pd
from mlpredictor.logging import logger
from mlpredictor.entity.config_entity import DataValidationConfig


# Data Validation Component
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_data(self):
        try:
            validation_status = None
            data = pd.read_csv(self.config.dataset_csv)

            all_column = data.columns
            all_schema = self.config.all_schema.keys()

            for col in all_column:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validation status: {validation_status}")


        except Exception as e:
            raise e
