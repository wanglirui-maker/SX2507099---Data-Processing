import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    简化版自动清洗（因无真实 LLM 调用时可本地模拟）
    - 删除全空列
    - 数值列用均值填充
    - 类别列用众数填充
    """
    # 删除全空列
    df = df.dropna(axis=1, how='all')
    
    # 分离数值和类别列
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(exclude='number').columns
    
    # 填充缺失值
    for col in num_cols:
        df[col].fillna(df[col].mean(), inplace=True)
    for col in cat_cols:
        mode_val = df[col].mode()
        if not mode_val.empty:
            df[col].fillna(mode_val[0], inplace=True)
        else:
            df[col].fillna("Unknown", inplace=True)
    
    return df
