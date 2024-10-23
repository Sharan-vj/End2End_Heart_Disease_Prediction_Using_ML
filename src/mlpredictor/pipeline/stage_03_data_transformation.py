# Import Dependencies
from mlpredictor.logging import logger
from mlpredictor.config.configuration import ConfigManager
from mlpredictor.components.data_transformation import DataTransformation


# Stage Name
STAGE_NAME = "DATA TRANSFORMATION"


# Data Transformation Pipeline
class DataTransformationPipeline:
    def __init__(self):
        pass


    def initiate_data_transformation(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform_dataset()


if __name__ == '__main__':
    try:
        logger.info(msg=f"STAGE {STAGE_NAME} STARTED")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(msg=f"STAGE {STAGE_NAME} COMPLETED")
    except Exception as e:
        raise e
