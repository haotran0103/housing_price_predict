import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.utils import save_objects
from src.exception import CusException
from src.logger import logging
import os



@dataclass
class DataTranformationConfig():
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessing.pkl')

class DataTranformation():
    def __init__(self):
        self.data_transformation_config = DataTranformationConfig()
    def get_data_transformer_obj(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info("category standard completed")
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("category encoder completed")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipelines", num_pipeline, numerical_columns),
                    ("cat_pipelines", cat_pipeline, categorical_columns),
                ]
            )
            
            return preprocessor
        except Exception as e:
            raise CusException(e,sys)
    
    def initate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("read training and test data set complete")
            
            preprocessing_obj = self.get_data_transformer_obj()
            target_column_names = "math_score"
            numerical_column_names = ["writing_score", "reading_score"]
            
            input_features_train_df = train_df.drop(columns=[target_column_names],axis=1)
            target_features_train_df = train_df[target_column_names]
            
            input_features_test_df = test_df.drop(columns=[target_column_names], axis=1)
            target_features_test_df = test_df[target_column_names]
            
            
            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[
                input_features_train_arr, np.array(target_features_train_df)
            ]
            test_arr = np.c_[
                input_features_test_arr, np.array(target_features_test_df)
            ]
            
            save_objects(
                self.data_transformation_config.preprocessor_obj_file_path,
                preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path, 
            )
        except Exception as e:
            raise CusException(e,sys)