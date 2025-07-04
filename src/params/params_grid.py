params = {
    "RandomForest": {
        # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
        # 'max_features':['sqrt','log2',None],
        "n_estimators": [8, 16, 32, 64, 128, 256]
    },
    "Decision Tree": {
        "criterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
        # 'splitter':['best','random'],
        # 'max_features':['sqrt','log2'],
    },
    "Adaboost": {
        "learning_rate": [0.1, 0.01, 0.5, 0.001],
        # 'loss':['linear','square','exponential'],
        "n_estimators": [8, 16, 32, 64, 128, 256],
    },
    "GradientBoost": {
        # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
        "learning_rate": [0.1, 0.01, 0.05, 0.001],
        "subsample": [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
        # 'criterion':['squared_error', 'friedman_mse'],
        # 'max_features':['auto','sqrt','log2'],
        "n_estimators": [8, 16, 32, 64, 128, 256],
    },
    "Linear Regression": {},
    "XGB": {
        "learning_rate": [0.1, 0.01, 0.05, 0.001],
        "n_estimators": [8, 16, 32, 64, 128, 256],
    },
    "Catboost": {
        "depth": [6, 8, 10],
        "learning_rate": [0.01, 0.05, 0.1],
        "iterations": [30, 50, 100],
    },
    "K Neighbour" : {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]  # 1 = Manhattan, 2 = Euclidean
    },

    "Ridge" : {
        'alpha': [0.01, 0.1, 1.0, 10.0, 100.0],
        'solver': ['auto', 'svd', 'cholesky', 'lsqr'],
        'fit_intercept': [True, False]
    },
    "Lasso" : {
        'alpha': [0.001, 0.01, 0.1, 1.0, 10.0],
        'fit_intercept': [True, False],
        'max_iter': [1000, 5000, 10000]
    }
}
