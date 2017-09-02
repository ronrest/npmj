from __future__ import print_function, division, unicode_literals
import os
import glob
import scipy
from scipy import misc
import numpy as np
from data import id2label, label2id, pickle2obj

# SETTINGS
pickle_file = "/path/to/data_pickle_file.pickle"  # Filepath to the pickled data

# DATA
# Load the pickle file created in the data.py file
data = pickle2obj(pickle_file)




