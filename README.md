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

### Figure 1a

#### First column

1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import bland_altman` which will reproduce the first column of figure 1a.


#### Second column
Same as above but using `./figures/ds109_notebook.ipynb`.

### Figure 1b
Same as 1a but using `./figures/ds120_notebook.ipynb`.

### Figure 2
#### Left sub-plot
1. From a Terminal, run:

    ```
    jupyter notebook ./figures/ds001_notebook.ipynb
    ```

3. In the notebook, run all the cells up to the cell starting with `from lib import dice`.

#### Middle sub-plot
Same as 2 left but using `./figures/ds109_notebook.ipynb`.

#### Right sub-plot
Same as 2 left but using `./figures/ds120_notebook.ipynb`.

<Instructions on how to use summary/derived data in the `results` directory to create figures and tables>

<Specify precise steps, including any datasets that need to be downloaded and path variables that need to be set>

## Reproducing full analysis

<Instructions on how to (1) obtain raw data; (2) process it to create summary/derived data in the `results`>

<Specify precise steps, including any datasets that need to be downloaded and path variables that need to be set>

# Contents overview

<Summarise what's in this repository>


# Software_Comparison
To run an SPM (FSL) analysis, set the variables in the process_ds001_SPM.m (process_ds001_FSL.py) script found in the /scripts/ directory appropriately for the study you wish to analyse, 
and then run the script in matlab by entering 'process_ds001_SPM.m' in the matlab command line while in the /scripts/ directory (or, run process_ds001_FSL.py from the terminal with 
'python process_ds001_FSL.py' when in the /scripts/ directory). This will create onsets, preprocess the data, and run first and group level analyses. 
