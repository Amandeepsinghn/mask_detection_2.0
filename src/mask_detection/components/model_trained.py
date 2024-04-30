import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from mask_detection.entity import model_training_config
from mask_detection.logging import logging
from mask_detection.utils import *
import yaml


import subprocess

class Base_model:
    def __init__(self, config:model_training_config):
        self.config = config
        
        
    def modify_data_yaml(self):
        with open('artifacts/data_ingestion/data.yaml','r') as f:
            data=yaml.safe_load(f)
            
        data['train']="C:/ml_projects/Dl_projects/Mask_detection_2.0/artifacts/data_ingestion/train"
        data['test']="C:/ml_projects/Dl_projects/Mask_detection_2.0/artifacts/data_ingestion/test"
        data['val']="C:/ml_projects/Dl_projects/Mask_detection_2.0/artifacts/data_ingestion/valid"
        
        with open("artifacts/data_ingestion/data.yaml",'w') as f:
            yaml.safe_dump(data,f)
            
    
    
        
    def model_training(self):
        command = [
            "yolo",
            f"task={self.config.task}",
            f"mode={self.config.mode}",
            f"model={self.config.model}",
            f"data={self.config.data_yaml}",
            f"epochs={self.config.epochs}",
            f"imgsz={self.config.img_size}",
            f"plots={self.config.plots}",
            f"save={self.config.updated_model_path}"
        ]
        subprocess.run(command)
        

        
