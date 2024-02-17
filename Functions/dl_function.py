import numpy as np
import pandas as pd


## Functions
def numeric_cols(dataset):
    numerics = dataset.select_dtypes(include= np.number).columns.tolist()
    return numerics

def cont_or_disc(dataset):
    numerics = numeric_cols(dataset)
    dict = {}
    for col in dataset[numerics]:
        total_count = dataset[col].count()
        unique_count = dataset[col].unique()
        len_unique = len(unique_count)
        type = 'Discrete' if len_unique < 10 else 'Continuous'
        dict[col] = [total_count, len_unique, type]
    results = pd.DataFrame.from_dict(dict,orient='index',columns=['total_count','len_unique', 'type'])
    return results

