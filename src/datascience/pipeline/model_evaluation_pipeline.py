from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = 'Model Evaluation Stage'


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
        onj = ModelEvaluationPipeline()
        onj.initiate_model_evaluation()
        logger.info(
            f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e
