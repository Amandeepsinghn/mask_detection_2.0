import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from mask_detection.entity import DataIngestionConfig
from mask_detection.logging import logging
from mask_detection.utils import *




class DataIngestion:
    
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file,mode='r') as zf:
            zf.extractall(os.path.join(self.config.unzip_dir))
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(self.config.source_url,filename=self.config.local_data_file)