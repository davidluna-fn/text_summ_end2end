from SummaVerse.config.configuration import ConfigurationManager
from SummaVerse.components.data_validation import DataValidation
from SummaVerse.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()