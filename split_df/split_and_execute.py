from multiprocessing_manager.run_function import RunFunctions
import pandas

def execute(func, df, n_splits = 8):
    dfs_list = []
    slice_size = int(len(df)/n_splits)

    while len(df) > 0:
        dfs_list.append(df.iloc[:slice_size])
        df = df.iloc[slice_size:]
    rf = RunFunctions(func, *dfs_list)

    return rf.return_values if rf.return_values else None