import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            # Verify if the source file exists
            source_file_path = "notebook/stud.csv"
            if not os.path.exists(source_file_path):
                logging.error(f"The file '{source_file_path}' does not exist.")
                raise FileNotFoundError(f"{source_file_path} not found.")
            
            # Read the data
            logging.info(f"Reading the dataset from {source_file_path}")
            df = pd.read_csv(source_file_path)
            logging.info("Dataset successfully read into a DataFrame.")

            # Create directory for artifacts if it does not exist
            artifacts_dir = os.path.dirname(self.ingestion_config.train_data_path)
            logging.info(f"Ensuring that the artifacts directory exists at: {artifacts_dir}")
            os.makedirs(artifacts_dir, exist_ok=True)
            logging.info("Artifacts directory is ready.")

            # Save raw data
            logging.info(f"Saving raw data to {self.ingestion_config.raw_data_path}")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            # Split the data into train and test sets
            logging.info("Initiating train-test split.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train-test split completed.")

            # Save train and test sets
            logging.info(f"Saving train data to {self.ingestion_config.train_data_path}")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info(f"Saving test data to {self.ingestion_config.test_data_path}")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion process completed successfully.")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("An error occurred during data ingestion.")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        obj.initiate_data_ingestion()
    except Exception as e:
        logging.error(f"Data ingestion failed: {e}")
