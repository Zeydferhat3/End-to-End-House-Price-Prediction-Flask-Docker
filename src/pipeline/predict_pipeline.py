import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from sklearn.preprocessing import LabelEncoder
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "proprocessor.pkl")
            print("Before Loading")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            cat_features = features.select_dtypes(include=['object', 'category']).columns

            for column in cat_features:
                label_encoder = LabelEncoder()
                features[column] = label_encoder.fit_transform(features[column])

            features = preprocessor.transform(features)
        
            preds = model.predict(features)
            return preds
    
        except Exception as e:
            raise CustomException(e, sys)



class CustomData:
    def __init__(  self,
        area: int,
        bedrooms: int,
        bathrooms:int,
        stories:int,
        mainroad: str,
        guestroom: str,
        basement: str,
        hotwaterheating: str,
        airconditioning: str,
        parking: int,
        prefarea: str,
        furnishingstatus: str):

        self.area = area

        self.bedrooms = bedrooms

        self.bathrooms = bathrooms
        self.stories = stories
        self.mainroad = mainroad

        self.guestroom = guestroom

        self.basement = basement

        self.hotwaterheating = hotwaterheating

        self.airconditioning = airconditioning

        self.parking = parking

        self.prefarea = prefarea
        
        self.furnishingstatus = furnishingstatus



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "area": [self.area],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "stories": [self.stories],
                "mainroad": [self.mainroad],
                "guestroom": [self.guestroom],
                "basement": [self.basement],
                "hotwaterheating": [self.hotwaterheating],
                "airconditioning": [self.airconditioning],
                "parking": [self.parking],
                "prefarea": [self.prefarea],
                "furnishingstatus": [self.furnishingstatus],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)