#%%
import pandas as pd
import os
import glob

# concatenando (UNION do sql) todos os jsons em uma lista
# %%
# extract

def data_extract_and_consolidate(folder: str) -> pd.DataFrame:
    files_json = glob.glob(os.path.join(folder, '*.json'))
    df_list = [pd.read_json(file) for file in files_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# %%
# transform function
def calculate_kpi_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# load data
def load_data(df: pd.DataFrame, format_exit: list):
    """
    Saves the DataFrame in the specified formats (e.g., "csv", "parquet").
    """
    for format_type in format_exit:
        if format_type == "csv":
            # Using index=False is common practice to avoid writing the DataFrame index as a column.
            df.to_csv("dados.csv", index=False)
            print("File 'dados.csv' created successfully.")
        elif format_type == "parquet":
            df.to_parquet("dados.parquet", index=False)
            print("File 'dados.parquet' created successfully.")

# %%

if __name__ == "__main__":
    folder_arg: str = 'data'
    data_frame = (data_extract_and_consolidate(folder=folder_arg))
    df_calculated = calculate_kpi_total_sales(data_frame)
    format_exit: list = ["csv","parquet"]
    load_data(df=df_calculated, format_exit=format_exit)