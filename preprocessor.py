import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_prepare(filepath):
    """
    Load and preprocess IoT sensor data from CSV.
    Returns normalised DataFrame and fitted scaler.
    """
    
    # 1. Load — set time as index
    df = pd.read_csv(filepath, index_col='time', parse_dates=True)
    
    # 2. Drop missing values
    df = df.dropna()
    
    # 3. Normalise to [0, 1]
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df),
        index=df.index,
        columns=df.columns
    )
    
    return df_scaled, scaler