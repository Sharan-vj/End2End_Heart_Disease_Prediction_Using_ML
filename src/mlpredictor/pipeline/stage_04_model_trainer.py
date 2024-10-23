# Import Dependencies
from mlpredictor.logging import logger
from mlpredictor.config.configuration import ConfigManager
from mlpredictor.components.model_trainer import ModelTrainer


# Stage Name
STAGE_NAME = "MODEL TRAINING"


# Model Training Pipeline
class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train_model()


if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
    except Exception as e:
        raise e