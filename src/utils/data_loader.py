import pandas as pd
from pathlib import Path


def load_data(path: Path):
    return pd.read_csv(path)
