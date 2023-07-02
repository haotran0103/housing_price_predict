import os 
import sys
from src.exception import CusException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv') 
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initate_data_ingestion(self):
        logging.info('entering data_ingestion')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('exported data')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('train test split data')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header=True)
            
            logging.info("ingestion completed successfully ")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CusException(e,sys)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initate_data_ingestion()

