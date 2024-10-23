# Import Dependencies
from mlpredictor.constants import *
from mlpredictor.entity.config_entity import *
from mlpredictor.utils.common import yaml_reader, create_directory


# Configuration Manager
class ConfigManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = yaml_reader(filepath=config_filepath, log=True)
        self.params = yaml_reader(filepath=params_filepath, log=True)
        self.schema = yaml_reader(filepath=schema_filepath, log=True)
        create_directory(directory_path=[self.config.artifacts_root], log=True)


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory(directory_path=[config.root_dir], log=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_url=config.dataset_url,
            dataset_raw=config.dataset_raw,
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directory(directory_path=[config.root_dir], log=True)

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            dataset_csv=config.dataset_csv,
            status_file=config.status_file,
            all_schema=schema
        )
        return data_validation_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directory(directory_path=[config.root_dir], log=True)

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            dataset_csv=config.dataset_csv
        )
        return data_transformation_config


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestClassifier
        schema = self.schema.TARGET_COLUMN
        create_directory(directory_path=[config.root_dir], log=True)

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_csv_file=config.train_csv_file,
            run_file=config.run_file,
            model_name=config.model_name,
            n_estimators=params.n_estimators,
            criterion=params.criterion,
            max_depth=params.max_depth,
            min_samples_split=params.min_samples_split,
            min_samples_leaf=params.min_samples_leaf,
            max_features=params.max_features,
            bootstrap=params.bootstrap,
            class_weight=params.class_weight,
            target_column=schema.name
        )
        return model_trainer_config
