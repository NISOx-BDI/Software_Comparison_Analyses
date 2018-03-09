# Exploring the Impact of Analysis Software on fMRI Results

Supporting code to perform the analyses and create the figures of the manuscript with the same title available at <ADD_BIORXIV_DOI_WITH_LINK>.

## How to cite

To cite this repository, please cite the corresponding manuscript: 

"Exploring the Impact of Analysis Software on fMRI Results" Alexander Bowring, Thomas E. Nichols, Camille MaumetTechnical Report bioRxiv: 1-<ADD_NUM_OF_PAGES>. doi: <ADD_DOI_WITH_LINK>. 

## Reproducing figures and tables

### Dependencies
To reproduce the figures, you will need to install the dependencies listed in `requirements.txt`, this can be done using pip with:
```
pip install -r requirements.txt
```

You will also need to have Jupyter notebook installed, we recommend using [Anaconda](https://conda.io/docs/user-guide/install/index.html) to perform the install.

### Fig. 1a

#### Left column

1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import bland_altman` which will reproduce the first column of figure 1a.


#### Right column
Same as Fig. 1 left but using `./figures/ds109_notebook.ipynb`.

### Fig. 1b
Same as 1a but using `./figures/ds120_notebook.ipynb`.

### Fig. 2
#### Left sub-plot
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import dice`.

#### Middle sub-plot
Same as Fig. 2 left but using `./figures/ds109_notebook.ipynb`.

#### Right sub-plot
Same as Fig. 2 left but using `./figures/ds120_notebook.ipynb`.

### Fig. 3

#### Left column
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import euler_characteristics`.

#### Right column
Same as Fig. 3 left but using `./figures/ds109_notebook.ipynb`.

### Fig. 4
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import plot_excursion_sets`.

### Fig. 5
#### Left column
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `bland_altman.bland_altman('Bland-Altman Plots: Permutation Tests'`.

#### Right column
Same as Fig. 5 left but using `./figures/ds109_notebook.ipynb`.

### Fig. 6
#### Left column
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `reload(bland_altman) bland_altman.bland_altman_intra('Bland-Altman Plots: Parametric vs Permutation'`.

#### Right column
Same as Fig. 6 left but using `./figures/ds109_notebook.ipynb`.

## Reproducing full analysis

### Raw data
To run the experiments included in the manuscript, raw data must be downloaded from [OpenfMRI.org](https://openfmri.org) and copied on your local computer:
 - ds000001 revision 2.0.4: https://openfmri.org/dataset/ds000001/
 - ds000109 revision 2.0.2: https://openfmri.org/dataset/ds000109/
 - ds000120 revision 1.0.0: https://openfmri.org/dataset/ds000120/

### Analysis of ds000001
Given:
 - `<PATH_TO_RAW_DATA>`: the path to the raw data for `ds000001` and
 - `<PATH_TO_OUTPUT>`: the path to the output folder where the results should be stored.

1. In `scripts/process_ds001_SPM.m` replace the values of `study_dir` and `results_dir` by `<PATH_TO_RAW_DATA>` and `<PATH_TO_OUTPUT>` respectively.

2. In `scripts/process_ds001_FSL.py` and `scripts/process_ds001_AFNI.py` replace the values of `raw_dir` and `results_dir` by `<PATH_TO_RAW_DATA>` and `<PATH_TO_OUTPUT>` respectively.

1. For the SPM analysis, inside Matlab run:

    ```
    addpath('scripts')
    addpath(fullfile('scripts', 'lib'))
    process_ds001_SPM
    ```
    
2. For the FSL analysis, from a terminal run:

    ```
    python scripts/process_ds001_FSL.py
    ```

3. For the AFNI analysis, from a terminal run:

    ```
    python scripts/process_ds001_AFNI.py
    ```

### Analysis of ds000109
Same as for ds000001, replacing all occurences of `001` by `109`.

### Analysis of ds000120
Same as for ds000001, replacing all occurences of `001` by `120`.

<Instructions on how to (1) obtain raw data; (2) process it to create summary/derived data in the `results`>

<Specify precise steps, including any datasets that need to be downloaded and path variables that need to be set>

# Contents overview

<Summarise what's in this repository>


# Software_Comparison
To run an SPM (FSL) analysis, set the variables in the process_ds001_SPM.m (process_ds001_FSL.py) script found in the /scripts/ directory appropriately for the study you wish to analyse, 
and then run the script in matlab by entering 'process_ds001_SPM.m' in the matlab command line while in the /scripts/ directory (or, run process_ds001_FSL.py from the terminal with 
'python process_ds001_FSL.py' when in the /scripts/ directory). This will create onsets, preprocess the data, and run first and group level analyses. 
