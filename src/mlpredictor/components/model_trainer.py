# Import Dependencies
import os
import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
from dotenv import load_dotenv
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from mlpredictor.logging import logger
from mlpredictor.entity.config_entity import ModelTrainerConfig
from mlpredictor.utils.common import save_mlflow_run, save_ml_model


# # Load environment variables from .env file
load_dotenv()

# Set up MLflow experiment
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")


# Model Trainer Component
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.EXPERIMENT_NAME = "Heart Disease Experiment"
    
    def train_model(self):
        train_data = pd.read_csv(self.config.train_csv_file)
        X_train = train_data.drop(self.config.target_column, axis=1)
        y_train = train_data[self.config.target_column]

        mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
        mlflow.set_experiment(experiment_name=self.EXPERIMENT_NAME)
        with mlflow.start_run() as run:
            run_id = run.info.run_id
            save_mlflow_run(run_id=run_id, run_file=Path(self.config.run_file))
            
            model = RandomForestClassifier(
                n_estimators=self.config.n_estimators,
                criterion=self.config.criterion,
                max_depth=self.config.max_depth,
                min_samples_split=self.config.min_samples_split,
                min_samples_leaf=self.config.min_samples_leaf,
                max_features=self.config.max_features,
                bootstrap=self.config.bootstrap,
                class_weight=self.config.class_weight
            )

            mlflow.log_param(key="n_estimators", value=self.config.n_estimators)
            mlflow.log_param(key="criterion", value=self.config.criterion)
            mlflow.log_param(key="max depth", value=self.config.max_depth)
            mlflow.log_param(key="min sample split", value=self.config.min_samples_split)
            mlflow.log_param(key="min sample leaf", value=self.config.min_samples_leaf)
            mlflow.log_param(key="max features", value=self.config.max_features)
            mlflow.log_param(key="bootstrap", value=self.config.bootstrap)
            mlflow.log_param(key="class weight", value=self.config.class_weight)


            model.fit(X=X_train, y=y_train)
            save_ml_model(model=model, model_path=Path(os.path.join(self.config.root_dir, self.config.model_name)))
            mlflow.sklearn.log_model(sk_model=model, artifact_path="model")
            mlflow.end_run()