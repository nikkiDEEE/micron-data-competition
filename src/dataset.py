from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd

from src.config import INTERIM_DATA_DIR, RAW_DATA_DIR

def convert_parquet_to_csv(input_dir=RAW_DATA_DIR):
    """
    Convert parquet files to a single CSV file.
    """
    logger.info(f"Converting parquet files in {input_dir} to dataframes")
    parquet_files = list(input_dir.glob("*.parquet"))

    incoming_df = pd.DataFrame()
    metro_df = pd.DataFrame()
    run_df = pd.DataFrame()

    for file in parquet_files:
        if file.name.startswith("incoming"):
            incoming_df = pd.concat([incoming_df, pd.read_parquet(file)])
        elif file.name.startswith("metro"):
            metro_df = pd.concat([metro_df, pd.read_parquet(file)])
        elif file.name.startswith("run"):
            run_df = pd.concat([run_df, pd.read_parquet(file)])
        else:
            logger.warning(f"Unknown file type: {file.name}")

    logger.info("Parquet files converted to dataframes")

    return incoming_df, metro_df, run_df



def main():
    pass

if __name__ == "__main__":
    main()
