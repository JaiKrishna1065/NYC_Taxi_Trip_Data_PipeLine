import pandas as pd

def extract_data(path):
    df = pd.read_parquet(path,engine='pyarrow')
    return df