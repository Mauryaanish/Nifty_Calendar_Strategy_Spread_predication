import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

@dataclass

class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts' , 'train.csv')
    test_data_path:str = os.path.join('artifacts' , 'test.csv')
    raw_data_path:str = os.path.join('artifacts' , 'raw.csv')

## create a class for Data ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion Method Starts')

        try:
            df = pd.read_excel(os.path.join('notebook/data' , 'Nifty_Spread_Data.xlsx'))
            logging.info('Dateset Read as pandas Dataframe and data cleaning starts')

            df.drop(['Date'] ,axis = 1, inplace = True)
            df['Remaining_day']=df['Remaining_day'].replace(3 , 4)
            df.drop(['Closing_price' , 'Strike_price'] , axis=1 , inplace = True)

            logging.info('Data Cleaning completed')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path , index=False)

            logging.info('Train Test Split')

            train_set,test_set = train_test_split(df , test_size=0.3 , random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path , index = False , header = True)
            train_set.to_csv(self.ingestion_config.test_data_path , index =False , header = True)

            logging.info('Ingestion of data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config. test_data_path
            )




        except Exception as e:
            logging.info('Exception Occured at data Ingestion stage')
            raise CustomException(e ,sys)


