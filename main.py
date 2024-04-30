from mask_detection.logging import logging
from mask_detection.pipeline.stage_01_data_ingestion import DataingestionTrainingPipeline
from mask_detection.pipeline.stage_02_model_training import ModelTrainingPipeline


STAGE_NAME="Data_ingestion"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataingestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e
     
STAGE_NAME="Preparing base model"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e