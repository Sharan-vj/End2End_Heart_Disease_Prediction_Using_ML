# Import Dependencies
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlpredictor.logging import logger
from mlpredictor.entity.config_entity import DataTransformationConfig


# Data Transformation Component
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_dataset(self):
        data = pd.read_csv(self.config.dataset_csv)
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info(msg="Splitted Dataset into Train and Test Sets")
        logger.info(msg=f"Train data shape: {train.shape}, Test data shape: {test.shape}")
        