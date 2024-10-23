# Import Dependencies
from mlpredictor.logging import logger
from mlpredictor.config.configuration import ConfigManager
from mlpredictor.components.data_validation import DataValidation


# Stage Name
STAGE_NAME = "DATA VALIDATION"


# Data Validation Pipeline
class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()


if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
    except Exception as e:
        raise e
