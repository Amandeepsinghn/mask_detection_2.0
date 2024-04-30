from src.mask_detection.constants import *
from src.mask_detection.utils import read_yaml,create_directories
from src.mask_detection.exception import AppException
import sys
from pathlib import Path
import os 
from mask_detection.entity import DataIngestionConfig,model_training_config




class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            source_url=config.source_url,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    
    def get_model_traning_config(self)->model_training_config:
        config=self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        model_return=model_training_config(
                root_dir=config.root_dir,
                updated_model_path=config.updated_model_path, 
                trained_model_mod=config.trained_model_mod,
                img_size=self.params.img_size,
                data_yaml=self.params.data_yaml,
                mode=self.params.mode,
                model=self.params.model,
                epochs=self.params.epochs, 
                plots=self.params.plots, 
                task=self.params.task     
                    )
        
        return model_return
        
        

