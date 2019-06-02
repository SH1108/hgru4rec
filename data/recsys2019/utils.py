import numpy as np
import pandas as pd

def get_name2idx(data, name):
    unique = data[name].unique()
    name2idx_dic = dict(pd.Series(np.arange(len(unique)), unique))
    return np.array([name2idx_dic[i] for i in data[name]])
