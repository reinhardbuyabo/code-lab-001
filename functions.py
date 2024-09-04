import pandas as pd

def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    print(f"Successfully read {file_path}")
    return df
