from pathlib import Path
from typing import Union, List

import fire
import h5py
from pandas import DataFrame


def main(data_dir: str, csv_dir: str):
    """
    Find .h5 file recursively in the data folder and unpack the h5 file to csv files. The h5 file should contain
    'reduced diffraction data' with '2theta' and 'main' inside. The each row inside the '2theta' and 'main' will be
    the first and second column in the csv file.

    Parameters
    ----------
    data_dir
        The directory where there are h5 files in it.
    csv_dir
        The directory to save all the csv file.

    Returns
    -------
    Multiple two-column csv file will be generated in the
    """
    csv_dir = Path(csv_dir)
    if not csv_dir.exists():
        csv_dir.mkdir()
    h5_files = Path(data_dir).rglob("*.h5")
    for h5_file in h5_files:
        dfs = unpack(h5_file)
        if dfs is not None:
            for n, df in enumerate(dfs):
                csv_file = csv_dir.joinpath(f"{h5_file.stem}_{n}.csv")
                write_df(df, csv_file)
    return


def unpack(h5_file: Union[str, Path]) -> Union[List[DataFrame], None]:
    """
    Read the h5 file and extract the information about '2theta' and 'main' and put it in pandas dataframes.

    Parameters
    ----------
    h5_file
        The path to the h5 file.

    Returns
    ------
    dfs
        A list of the dataframe of '2theta' and 'main'. If failed, return None.
    """
    path = Path(h5_file)
    data = h5py.File(path, "r")
    if "reduced diffraction data" in data:
        diff_data = data['reduced diffraction data']
        if '2theta' in diff_data and 'main' in diff_data:
            twothetas = diff_data['2theta']
            intensities = diff_data['main']
        else:
            print(
                f"Processing failed for the file {path.name}. No key named '2theta' or 'main' in 'reduced diffraction data'"
            )
            return None
    else:
        print(
            f"Processing failed for the file {path.name}. No key named 'reduced diffraction data'"
        )
        return None

    dfs = []
    assert twothetas.shape == intensities.shape
    for twotheta, intensity in zip(twothetas, intensities):
        dct = {
            "2theta": twotheta,
            "intensity": intensity
        }
        df = DataFrame(dct)
        dfs.append(df)
    return dfs


def write_df(df: DataFrame, file_name: Union[str, Path]):
    """
    Write the data frame to the csv file.

    Parameters
    ----------
    df
        The pandas dataframe.
    file_name
        The csv file name.
    """
    df.to_csv(file_name, index=False)
    return


if __name__ == "__main__":
    fire.Fire(main)
