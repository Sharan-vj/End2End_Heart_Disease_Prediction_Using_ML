# Import Dependencies
import os 
import yaml
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any
from pathlib import Path
from winePredictor.logging import logger


@ensure_annotations
def yaml_reader(filepath: Path, log: bool) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        filepath (Path): The path to the YAML file to be read.
        log (bool): If True, logs a message indicating successful loading of the YAML file.

    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other exception occurs during the reading process.
    """
    try:
        with open(filepath, 'r') as file:
            content = yaml.safe_load(file)
            if log:
                logger.info(msg=f"Yaml file: {filepath} loaded successfully.")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e


def create_directory(directory_path: list, log: bool) -> None:
    """
    Creates directories specified in the 'directory_path' list.

    Args:
        directory_path (list): A list of paths to the directories to be created.
        log (bool): If True, logs a message indicating successful creation of the directories.

    Returns:
        None

    Raises:
        Exception: If any other exception occurs during the directory creation process.
    """
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if log:
            logger.info(msg=f"{directory_path} Directory created successfully")


def save_json(path: Path, data: dict, log: bool) -> None:
    """
    Saves a JSON file from the given data dictionary to the specified path.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): The data to be saved as a JSON file.
        log (bool): If True, logs a message indicating successful saving of the JSON file.

    Returns:
        None

    Raises:
        Exception: If any other exception occurs during the JSON file saving process.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        if log:
            logger.info(msg=f"Json file saved to {path}")


def load_json(path: Path, log: bool) -> ConfigBox:
    """
    Loads a JSON file from the specified path and returns its content as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file to be loaded.
        log (bool): If True, logs a message indicating successful loading of the JSON file.

    Returns:
        ConfigBox: The content of the JSON file as a ConfigBox object.

    Raises:
        Exception: If any other exception occurs during the JSON file loading process.
    """
    with open(path, 'r') as f:
        content = json.load(f)
        if log:
            logger.info(msg=f"Json file loaded to {path}")
        return ConfigBox(content)


def save_mlflow_run(run_id: str, run_file: Path) -> None:
    """
    Saves the given run_id to the specified run_file.

    Args:
        run_id (str): The unique identifier for the MLflow run.
        run_file (Path): The path to the file where the run_id will be saved.

    Returns:
        None

    Raises:
        Exception: If any other exception occurs during the file saving process.
    """
    run_file.parent.mkdir(parents=True, exist_ok=True)
    with run_file.open('a') as f:
        f.write(f"RUN ID: {run_id}\n")


def load_mlflow_run(run_file: Path) -> str:
    """
    Loads the most recent run ID from the specified run file.

    Args:
        run_file (Path): The path to the file containing the MLflow run IDs.

    Returns:
        str: The most recent run ID found in the file.

    Raises:
        FileNotFoundError: If the specified run file does not exist.
        ValueError: If the file is empty.
    """
    if not run_file.exists():
        raise FileNotFoundError(f"{run_file} does not exist.")

    with run_file.open('r') as f:
        lines = f.readlines()

    if not lines:
        raise ValueError("The file is empty.")

    last_line = lines[-1].strip()
    run_id_str = last_line.split("RUN ID: ")[-1]

    return str(run_id_str)


def save_ml_model(model, model_path: Path) -> None:
    """
    Saves a machine learning model saved using joblib to the specified path.

    Args:
        model (Any): The machine learning model to be saved.
        model_path (Path): The path to the file where the serialized machine learning model will be saved.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified model file does not exist.

    Saves the given model to the specified model_path. The model_path directory is created if it does not exist.
    """
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved at: {model_path}")


def load_ml_model(model_path: Path) -> Any:
    """
    Loads a machine learning model saved using joblib from the specified path.

    Args:
        model_path (Path): The path to the file containing the serialized machine learning model.

    Returns:
        Any: The loaded machine learning model.

    Raises:
        FileNotFoundError: If the specified model file does not exist.
    """
    if not model_path.exists():
        raise FileNotFoundError(f"{model_path} does not exist.")

    model = joblib.load(model_path)
    print(f"Model loaded from: {model_path}")
    return model


def get_size(path: Path) -> str:
    """
    Calculates the size of a file or directory in kilobytes (KB).

    Args:
        path (Path): The path to the file or directory whose size is to be calculated.

    Returns:
        str: The size of the file or directory in kilobytes (KB), rounded to the nearest integer.
    """
    size_kb = round(os.path.getsize(path) / 1024)
    return f"{size_kb} KB"
