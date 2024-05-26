#Usual Imports
import os
import sys
import json
import numpy as np
from tqdm import tqdm

# plotting library
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio

# append path to custom scripts
sys.path.append('/kaggle/input/lidar-od-scripts/gpuVersion/gpuVersion/')

# DL Imports
import torch
import torch.nn as nn

# custom imports
from visual_utils import plot_pc_data3d, plot_bboxes_3d

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

pio.renderers.default = "browser"

#mesh
import open3d