import os
import sys
import dill

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(x_train, y_train, x_test, y_test, models: dict, param: dict):
    try:
        report = {}
        trained_models = {}

        for name, model in models.items():
            para = param.get(name, {})  
            gs = GridSearchCV(model, para, cv=3, scoring='r2', n_jobs=-1)
            gs.fit(x_train, y_train)

            best_model = gs.best_estimator_
            y_train_pred = best_model.predict(x_train)
            y_test_pred = best_model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[name] = test_model_score
            trained_models[name] = best_model

        return report, trained_models

    except Exception as e:
        raise CustomException(e, sys)