# Import Dependencies
from pathlib import Path
from dataclasses import dataclass


# Data Ingestion Config
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_url: str
    dataset_raw: Path


# Data Validation Config
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    dataset_csv: Path
    status_file: str
    all_schema: dict


# Data Transformation Config
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    dataset_csv: Path


# Model Trainer Config
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_csv_file: Path
    run_file: Path
    model_name: str
    n_estimators: int
    criterion: str
    max_depth: int
    min_samples_split: int
    min_samples_leaf: int
    max_features: str
    bootstrap: bool
    class_weight: str
    target_column: str


# Model Evaluation Config
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_csv_file: Path
    run_file: Path
    trained_model: Path
    final_model: Path
    metrics_file: Path
    all_params: dict
    target_column: str