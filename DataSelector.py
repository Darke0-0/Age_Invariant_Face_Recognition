import numpy as np
import pandas as pd
import os

def data_select(arg):

    if arg.dataset == 'cacd':

        total_data = pd.read_csv(os.path.join(arg.data_path, 'CACD.csv'))
        train_data = total_data.loc[total_data['fold'] == arg.experiment_setting].reset_index(drop=True)
        test_data = total_data.loc[total_data['fold'] == 'test'].reset_index(drop=True)

        age_min, age_max = train_data['age'].min(), train_data['age'].max()

        age_group = [[int(age_min), 23], [19, 29], [24, 38], [30, 48], [39, int(age_max)]]

        if arg.experiment_setting == 'train':
            sampling = True
            sample_rate = 0.05

        elif arg.experiment_setting == 'val':
            sampling = False
            sample_rate = -1

    return train_data, test_data, age_group, sampling, sample_rate