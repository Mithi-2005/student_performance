import sys
import os
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from catboost import CatBoostRegressor  # type: ignore
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model
from src.params.params_grid import params


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_training(self, train_arr, test_arr):
        try:
            x_train, x_test, y_train, y_test = (
                train_arr[:, :-1],
                test_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, -1],
            )

            models = {
                "RandomForest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Adaboost": AdaBoostRegressor(),
                "GradientBoost": GradientBoostingRegressor(),
                "K Neighbour": KNeighborsRegressor(),
                "XGB": XGBRegressor(),
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "Catboost": CatBoostRegressor(),
            }

            model_report, trained_models = evaluate_model(
                x_train, y_train, x_test, y_test, models,params
            )

            best_model_scrore = max(list(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_scrore)
            ]

            best_model = trained_models[best_model_name]

            if best_model_scrore < 0.6:
                raise CustomException("No Best Model Found")

            logging.info("Best Model FOund in Model Found")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            predicted = best_model.predict(x_test)

            r2 = r2_score(y_test, predicted)

            return r2

        except Exception as e:
            raise CustomException(e, sys)
