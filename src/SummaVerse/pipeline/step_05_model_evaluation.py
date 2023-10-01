from SummaVerse.config.configuration import ConfigurationManager
from SummaVerse.components.model_evaluation import ModelEvaluation
from SummaVerse.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()