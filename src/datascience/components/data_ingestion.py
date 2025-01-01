import os
import urllib.request as request
from src.datascience import logger
from src.datascience.entity.config_entity import (DataIngestionConfig)
import zipfile


class DataIngestion:
    def __init__(self, config=DataIngestionConfig):
        self.config = config

    # Downloading the data zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(
                f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_path)
