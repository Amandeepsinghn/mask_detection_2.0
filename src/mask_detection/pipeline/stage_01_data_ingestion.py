from mask_detection.config import ConfigurationManager
from mask_detection.components import DataIngestion
from mask_detection.logging import logging









class DataingestionTrainingPipeline:
    def __init__(self):
        pass
        
    def main(self):
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_and_clean()
    
