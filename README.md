# h5xrd
A CLI software to unpack h5 files from the synchrotron source

## Installation

Welcome to h5xrd! The installation uses [Anaconda](https://anaconda.org/). Open your terminal, create the environment.

``conda env create -f environment.yml python=3.8``

1. Activate the environment.

``conda create h5xrd``

2. Fork and clone the github repo or download and unzip it. Open the terminal, cd into the repo and pip install it (development mode "-e" is recommended).

``pip install -e .``

3. (Optional) Add an alias to the program in the bash profile. Substitute the content in "<>" to the path on your computer.

``alias h5xrd="python <path to h5xrd/main.py>"``

## Usage

If you have a folder named "data" and there are h5 files inside and you would like to extract the '2theta' and 'main'
data in each h5 files and save them as csv files in a folder named "csv", then, run the following command in the
directory of "h5xrd". Substitute the content in "<>" to the path on your computer.

``python main.py <path to data folder> <path to csv folder>``

If you have already done the step 3 in the installation, then you can run the following command instead.
It doesn't have to be run inside the h5xrd folder.

``h5xrd <path to data folder> <path to csv folder>``