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
