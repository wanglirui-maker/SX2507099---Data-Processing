import pandas as pd

def load_data(file_path: str):
    """加载 CSV 数据"""
    return pd.read_csv(file_path)
