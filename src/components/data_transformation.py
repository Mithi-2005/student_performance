import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer ## For imputing missing values
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTranformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_tranformer_obj(self):
        '''
            this function is responsible for data transformation
        '''
        try:
            numerical_features=["reading score",'writing score']
            categorical_features=['gender','race/ethnicity','parental level of education','lunch','test preparation course']
            
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('Standard Scaler',StandardScaler())
                ]
            )
            
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('OHE',OneHotEncoder()),
                    ('Scaler',StandardScaler(with_mean=False))
                ]
            )
            
            logging.info('Numerical Columns Standard Scaling Completed')
            logging.info('Categorical Columns Encoding Completed')
            
            preproccesor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_features),
                    ('cat_pipeline',cat_pipeline,categorical_features),
                ]
            )
            
            return preproccesor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            
            logging.info("Read Train and Test Data Successfully ")
            
            logging.info('Obtaining Preprocessor object')
            
            preprocessing_obj=self.get_data_tranformer_obj()
            
            target_column_name='math score'
            numerical_features=["reading score",'writing score']
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            
            logging.info("Applying preprocessing obj on training andd testing dataframe")
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            
            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            
            logging.info('Saving Preprocessing Object')
            
            save_object(
                
                file_path=self.data_transformation_config.preprocessor_ob_file_path,
                obj=preprocessing_obj
                
            )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        