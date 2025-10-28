"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views
'''
def load_inflammation_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)
    return list(data)
'''

def compute_standard_deviation_by_day(data):
    """Calculate the standard deviation by day for a 2d inflammation data array."""
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    # views.visualize(graph_data)
    return daily_standard_deviation

class CSVDataSource:
    """Data source for loading inflammation data from CSV files in a directory."""
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        else: 
            pass
        data = map(models.load_csv, data_file_paths)
        return list(data)
    
class JSONDataSource:
    """Data source for loading inflammation data from JSON files in a directory."""
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = map(models.load_json, data_file_paths)
        return list(data)

# Not sure where infiles is defined
pathway = "/home/jk8173/python-intermediate-inflammation/data/"
_, extension = os.path.splitext("/home/jk8173/python-intermediate-inflammation/data/inflammation-01.csv")
if extension == '.json':
  data_source = JSONDataSource(os.path.dirname(pathway))
elif extension == '.csv':
  data_source = CSVDataSource(os.path.dirname(pathway))
else:
  raise ValueError(f'Unsupported data file format: {extension}')
analyse_data(data_source)