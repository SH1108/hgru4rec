import numpy as np
import pandas as pd
import subprocess
import argparse

from utils import get_name2idx

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='mini_train.csv')
args = parser.parse_args()

idxed_key = ['user_id', 'reference', 'session_id']

def preprocess(path):
    data = pd.read_csv(path)
    for key in idxed_key:
        data[key] = get_name2idx(data, key)
    data = data.rename(columns={'reference': 'item_id'})
    return data

def main():
    data = preprocess(args.path)
    data.to_csv('preprocessed_'+args.path)
if __name__ == '__main__':
    main()
