import logging
import pickle
import os
import pandas as pd
import numpy as np

from random import randrange
from statistics import mode


def get_row(dataframe, position):
    """Select a row in csv file
    Arguments:
        path {str} -- path to the csv file
        position {int} -- position of the row
    Returns:
        numpy.ndarray -- array of landmarks of a frame (row)
    """
    selected_row = dataframe.iloc[position].values.tolist()
    return np.array([selected_row[i:i+2] for i in range(0, 42, 2)])


def start_predict(output_file_path, k_frames=10):
    classification_list = []
    model_binary_file = "src/lib/knnclassifier_file"

    logging.info("Starting prediction.")
    model = pickle.load(open(os.path.abspath(model_binary_file), "rb"))

    dataframe = pd.read_csv(output_file_path, index_col=False)

    for _ in range(1, k_frames):
        frame = get_row(dataframe, randrange(1, len(dataframe)))
        frame = frame.reshape(1, -1)
        classification_list.append(model.predict(frame)[0])

    return mode(classification_list)
