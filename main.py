from src.datascience import logger
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    onj = DataValidationTrainingPipeline()
    onj.initiate_data_validation()
    logger.info(
        f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
