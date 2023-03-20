# Demo of Clinica

This repository is intented to show a typical pipeline when working with images
in a clinical context and how [Clinica](https://www.clinica.run/)  can be
simplify this task.

## Install the demo

Create a conda environment and use poetry to install dependencies inside:

```
conda env create --file environment.yml -p ./env
conda activate ./env
poetry install

```
In order to share developments and to facilitate the review task, the contributions
must be done in the form of Python script.

Then use jupytext to convert the pythos scripts into Jupyter notebooks

```
jupytext --to notebook file.py --output file.ipynb
```

## Innovaheart 2023

### Steps of the demo

1. Connect to a XNAT DB and download images
2. Convert images to nifty
3. Use a pydra pipeline 
