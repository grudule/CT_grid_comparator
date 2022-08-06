from grids_diff_generator import grid_comparator
from showing_volume_scroll_bar import IndexTracker, showIMG
import glob
from matplotlib.colors import LogNorm
import os 
import numpy as np
import re

reference_grid = np.load(r"C:\Users\Alexandre\Desktop\results_abstract_CUMP2002\Référence 180 positions\root2Array_doses.npy")
list_result = glob.glob(r"C:\Users\Alexandre\Desktop\results_abstract_CUMP2002\mesures\*\root2Array_doses.npy", recursive=True)
index = 1
path_to_folder_results = r'C:\Users\Alexandre\Desktop\results_abstract_CUMP2002\error_grids'
# if not os.path.exists(path_to_folder_results):
#     os.makedirs(path_to_folder_results)
# for grid_dose in list_result:
    #print(grid_dose)
    # grid = np.load(grid_dose)
    # position = 10*index
    # position = f"{180-position}_positions"
    # if position == "0_positions":
    #     position = "1_position"
    # path_to_results = fr"{path_to_folder_results}\{position}"
    # if not os.path.exists(path_to_results):
    #     os.makedirs(path_to_results)
    # grids = grid_comparator(reference_grid, grid,  path_to_results, position)
    # index += 1
list_result = glob.glob(r"C:\Users\Alexandre\Desktop\results_abstract_CUMP2002\error_grids\*\*_diff_grid*.npy", recursive=True)
for i in list_result:
    splited_path = i.replace("\\", " ").split()
    name = splited_path[-1]
    index = [int(s) for s in re.findall(r'-?\d+\.?\d*', name)]
    print(index)
    volume = np.load(i)
    print(np.mean(volume))
    showIMG(volume, positions=index[0])