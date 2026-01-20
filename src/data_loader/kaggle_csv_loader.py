import os
from pathlib import Path
import pandas as pd
from typing import Union
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleCSVLoader:
    
    def __init__(
            self,
            dataset_name: str,
            csv_filename: str,
            raw_data_dir: Union[str, Path] = 'data/raw'
    ):
        """
        Parameters

        dataset_name: str
            Kaggle dataset identifier
        csv_filename: str
            Name of the CVS file inside the dataset
        raw_data_dir: str
            Directory where raw data will be stored
        """

        self.dataset_name = dataset_name
        self.csv_filename = csv_filename
        self.raw_data_dir = Path(raw_data_dir)
        self.raw_data_dir.mkdir(parents=True, exist_ok=True)

        self.api = KaggleApi()
        self.api.authenticate()

    def download_dataset(self) -> Path:
        print('Downloading the raw dataset from Kaggle')
        self.api.dataset_download_files(
            self.dataset_name,
            path = self.raw_data_dir,
            unzip = True
        )
        
    def load_csv(self) -> pd.DataFrame:
        
        csv_path = self.raw_data_dir / self.csv_filename

        if not csv_path.exists():
            raise FileNotFoundError(
                f'{self.csv_filename} not found in {self.raw_data_dir}'
            )
        
        print('Loading the target csv into a DataFrame')
        return pd.read_csv(csv_path)
        
    def run(self) -> pd.DataFrame:
        """
        Running the full pipeline for KaggleCSVLoader download -> load CSV
        """
        self.download_dataset()
        return self.load_csv()
