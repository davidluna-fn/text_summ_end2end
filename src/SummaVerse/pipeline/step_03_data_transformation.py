from SummaVerse.config.configuration import ConfigurationManager
from SummaVerse.components.data_transformation import DataTransformation
from SummaVerse.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()