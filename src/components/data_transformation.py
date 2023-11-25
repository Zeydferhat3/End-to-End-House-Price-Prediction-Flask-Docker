import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:

            numerical_columns = ["area","bedrooms",	"bathrooms"	,"stories","parking","mainroad"	,"guestroom"	,"basement",	"hotwaterheating"	,"airconditioning"	,"prefarea"	,"furnishingstatus" ] 
            
            num_pipeline= Pipeline(
                steps=[
                ("scaler",StandardScaler())
                ]
            )

    
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                
                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            preprocessing_obj=self.get_data_transformer_object()
            
            logging.info("obtained preprocessing object")

            target_column_name="price"
            
            x_train_df=train_df.drop(columns=[target_column_name],axis=1)
            y_train_df=train_df[target_column_name]

            x_test_df=test_df.drop(columns=[target_column_name],axis=1)
            y_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            cat_features = [ "mainroad",	"guestroom",	"basement",	"hotwaterheating",	"airconditioning",		"prefarea"	,"furnishingstatus"]
          
            for column in cat_features:
                label_encoder = LabelEncoder()
                x_train_df[column] = label_encoder.fit_transform(x_train_df[column])
                x_test_df[column] = label_encoder.fit_transform(x_test_df[column])

            xx_train=preprocessing_obj.fit_transform(x_train_df)
            xx_test=preprocessing_obj.transform(x_test_df)

            train_arr = np.c_[xx_train, np.array(y_train_df)]
            test_arr = np.c_[xx_test, np.array(y_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)