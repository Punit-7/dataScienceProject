from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPIpeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPIpeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    onj = DataIngestionTrainingPIpeline()
    onj.initiate_data_ingestion()
    logger.info(
        f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

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

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    onj = DataTransformationTrainingPIpeline()
    onj.initiate_data_transformation()
    logger.info(
        f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    onj = ModelTrainerPipeline()
    onj.initiate_model_training()
    logger.info(
        f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    onj = ModelEvaluationPipeline()
    onj.initiate_model_evaluation()
    logger.info(
        f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
