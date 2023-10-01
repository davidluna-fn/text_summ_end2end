from SummaVerse.config.configuration import ConfigurationManager
from SummaVerse.components.model_trainer import ModelTrainer
from SummaVerse.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()