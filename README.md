# `catmap`

![Build/Test Workflow](https://github.com/marissafujimoto/catmap/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/marissafujimoto/catmap/badge.svg?branch=main)](https://coveralls.io/github/marissafujimoto/catmap?branch=main)

A python based map of cancer transcriptomics. Written in python and currently in development.

## What is `catmap`?

`catmap` stands for **ca**(ncer) **t**(ranscriptomics) **map**. It is a data visualization application and tool used to visualize and project single cell gene expression data from cancer cells. The name `catmap` is inspired by the coats of calico cats where X chromosome inactivation combined with other genetic conditions result in distinct patches of orange, black, and white fur.

## Questions of Interest

### What is the topology of cancer in terms of gene expression? How does that correlate with projected phenotype labels?

`catmap` is an application which dimensionally reduces single cell gene expression datasets and visualizes them. Furthermore `catmap` allows projecting arbitrary labels onto the points (e.g. individual, cancer stage, patient demographics, cell type).

*There are many approaches to dimensionality reduction including PCA, t-SNE, UMAP, VAE. This project will investigate these techniques and we hope provide toggles between models if useful.*

*For now `catmap` focuses on non small cell lung cancer, but we hope to expand it's relevancy to other cancer types or even genetic conditions.*

### Given a new tissue sample, can we project these new cells onto the known database of cancer cells?

Current approaches to visualizing single cell gene expression produce static visualizations which don't allow investigation of new samples. `catmap` allows new data to be projected onto the existing map. Using projected phenotypes from the database of cells we can predict the phenotype of new samples. One question might be to ask how resistant to chemotherapy do we predict a new patient to be based on our knowledge of past patients.

*This is an unproven technique and has many challenges to overcome in terms of correcting for the batch effects between the reference samples and the new sample, but we hope to test its feasibility and provide some measure of effectiveness.*

## Summary of `catmap` Goals

We want to produce an application which presents a visualization of cancer transcriptomes and allows dynamic labels and filters to be applied. This interactive visualization is our minimum goal. One stretch goal is to implement this functionality for multiple cancer types and with different forms of dimensionality reduction.

Furthermore we hope to support the projection of new observations onto the visualization and provide relevant phenotypic predictions / classifications based upon the new observations similarity to our known database.

## Data

We are using the data from a meta-analysis of non-small-cell-lung cancer data sets as well as a dataset on colon cancer.

https://www.nature.com/articles/s41597-023-02074-6

https://singlecell.broadinstitute.org/single_cell/study/SCP1162/human-colon-cancer-atlas-c295

## Installation Instructions

catmap is currently not available on package manager (e.g. PyPI). Instructions to build from source are below.

First pull the git repository:

```
git clone git@github.com:marissafujimoto/catmap.git
```

Within catmap folder, install dependencies (requires conda):

```
cd catmap
conda env create -f environment.yml
conda activate catmap_env
```

Install catmap from source. Run from the root catmap folder where `pyproject.toml` is:

```
pip install .
```

The install script adds a command line tool called `catmap` to your path. To launch catmap from any directory:

```
catmap
```

Follow the instructions prompted in the command line for any streamlit related setup. Then open one of the links (e.g. localhost).

## Usage Instructions

To see more detailed instructions on usage see [usage examples](examples/usage_examples.md).

## Contact

For any issues or questions, open an issue via [github issues](https://github.com/marissafujimoto/catmap/issues).
