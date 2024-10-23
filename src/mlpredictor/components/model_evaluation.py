# Import Dependencies
import os
import pandas as pd
import mlflow
import mlflow.sklearn
from pathlib import Path
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score, f1_score
from mlpredictor.entity.config_entity import ModelEvaluationConfig
from mlpredictor.utils.common import load_ml_model, save_ml_model
from mlpredictor.utils.common import load_mlflow_run, save_json


# Load environment variables from .env file
load_dotenv()

# Set up MLflow experiment
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")


# Model Evaluation Component
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.EXPERIMENT_NAME = "Heart Disease Experiment"


    def error_report(self, actuals, predicted):
        ac = accuracy_score(y_true=actuals, y_pred=predicted)
        f1 = f1_score(y_true=actuals, y_pred=predicted)
        return ac, f1
    

    def evaluate_model(self):
        test_data = pd.read_csv(self.config.test_csv_file)
        X_test = test_data.drop(labels=self.config.target_column, axis=1)
        y_test = test_data[self.config.target_column]
        trained_model = load_ml_model(model_path=Path(self.config.trained_model))

        mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
        mlflow.set_experiment(experiment_name=self.EXPERIMENT_NAME)
        run_id = load_mlflow_run(run_file=Path(self.config.run_file))

        with mlflow.start_run(run_id=run_id) as run:
            pred = trained_model.predict(X_test)
            ac, f1 = self.error_report(actuals=y_test, predicted=pred)

            scores = {
                "accuracy": ac,
                "f1_score": f1
            }
            
            save_json(path=Path(self.config.metrics_file), data=scores, log=True)
            mlflow.log_metric(key="accuracy score", value=ac)
            mlflow.log_metric(key="f1_score", value=f1)

            if ac >=0.75:
                save_json(path=Path(self.config.metrics_file), data=scores, log=True)
                save_ml_model(model=trained_model, model_path=Path(self.config.final_model))
            mlflow.end_run()
