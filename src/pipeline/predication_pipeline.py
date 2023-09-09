import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self , features):
        try:
            preprocessor_path = os.path.join('artifacts' , 'preprocessor.pkl')
            model_path = os.path.join('artifacts' , 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info('Exception occured in prediction')
            raise CustomException(e,sys)     

class CustomData:

    def __init__(self,
                Day : str,
                Remaining_day : int,
                Vix : float,
                Moment_in_vix : float,
                Moment_in_price : float,
                Option_type:str,
                ):
        
        self.Day =  Day
        self.Remaining_day = Remaining_day
        self.Vix = Vix 
        self.Moment_in_vix = Moment_in_vix
        self.Moment_in_price = Moment_in_price
        self.Option_type  = Option_type

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Day' : [self.Day],
                'Remaining_day' : [self.Remaining_day],
                'Vix' : [self.Vix],
                'Moment_in_vix':[self.Moment_in_vix],
                'Moment_in_price' : [self.Moment_in_price],
                'Option_type' : [self.Option_type]
                
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e ,sys)


         