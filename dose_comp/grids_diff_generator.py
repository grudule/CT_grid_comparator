import numpy as np


### This mocdule generate generates 2 array, the difference between one array and the second, and one with the % in the diff.  
### If the saving option is activated then it will save both grids in .npy files 


def grid_comparator(reference_grid:np.array, grid2:np.array, path_to_results:str, index:str ="0", saving:bool=True) -> list:
    total_grid = reference_grid + grid2
    diff_grid = reference_grid - grid2
    diff_mean_grid = (diff_grid / total_grid) * 100
    if saving:
        np.save(fr"{path_to_results}/_diff_grid_{index}.npy", diff_grid)
        np.save(fr"{path_to_results}/diff_mean_grid_{index}.npy", diff_mean_grid)
    return [diff_grid, diff_mean_grid]