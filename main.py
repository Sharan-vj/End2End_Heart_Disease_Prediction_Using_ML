# Import Dependencies
from mlpredictor.logging import logger
from mlpredictor.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlpredictor.pipeline.stage_02_data_validation import DataValidationPipeline
from mlpredictor.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlpredictor.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from mlpredictor.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


# Data Ingestion Pipeline
STAGE_NAME = "DATA INGESTION"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
except Exception as e:
    raise e


# Data Validation Pipeline
STAGE_NAME = "DATA VALIDATION"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
except Exception as e:
    raise e


# Data Transformation Pipeline
STAGE_NAME = "DATA TRANSFORMATION"
try:
    logger.info(msg=f"STAGE {STAGE_NAME} STARTED")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(msg=f"STAGE {STAGE_NAME} COMPLETED")
except Exception as e:
    raise e


# Model Training Pipeline
STAGE_NAME = "MODEL TRAINING"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
except Exception as e:
    raise e


# Model Evaluation Pipeline
STAGE_NAME = "MODEL EVALUATION"
try:
    logger.info(msg=f"STAGE {STAGE_NAME} STARTED")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(msg=f"STAGE {STAGE_NAME} COMPLETED")
except Exception as e:
    raise e
