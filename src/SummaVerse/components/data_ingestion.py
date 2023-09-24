import os

import zipfile
from pathlib import Path
import urllib.request as request

from SummaVerse.logging import logger
from SummaVerse.utils.common import get_size
from SummaVerse.entity  import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file 
            )
            logger.info(f'{filename} download with following parameters: \n{header}')
        else:
            logger.info(f'Already exists of size {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """ Extracts the zip file to the local directory """
        
        unzip_path = self.config.unzip_dir 
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
