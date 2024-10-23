# Import Dependencies
from pathlib import Path
from dataclasses import dataclass


# Data Ingestion Config
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_url: str
    dataset_raw: Path
