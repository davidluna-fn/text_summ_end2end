from SummaVerse.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from SummaVerse.pipeline.step_02_data_validation import DataValidationTrainingPipeline
from SummaVerse.logging import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<< ')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.run()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\nx=====================x')
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<< ')
    data_validation = DataValidationTrainingPipeline()
    data_validation.run()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\nx=====================x')
except Exception as e:
    logger.exception(e)
    raise e
