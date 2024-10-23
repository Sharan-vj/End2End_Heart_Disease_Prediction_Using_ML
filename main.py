# Import Dependencies
from mlpredictor.logging import logger
from mlpredictor.pipeline.stage_01_data_ingestion import DataIngestionPipeline


# Data Ingestion Pipeline
STAGE_NAME = "DATA INGESTION"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
except Exception as e:
    raise e
