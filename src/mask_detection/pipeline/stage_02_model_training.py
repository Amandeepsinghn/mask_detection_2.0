from mask_detection.config import ConfigurationManager
from mask_detection.components import model_trained,Base_model
from mask_detection.logging import logging
import time








class ModelTrainingPipeline:
    def __init__(self):
        pass
        
    def main(self):
            mod=ConfigurationManager()
            mod1=mod.get_model_traning_config()
            base=Base_model(mod1)
            base.modify_data_yaml()
            
            time.sleep(5)
            base.model_training()

    