# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.5'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown]
# ![clinica_logo](https://aramislab.paris.inria.fr/clinica/files/clinica_logo/Clinica_banner.png)
# # Processing medical images in a Clinical environment
#
# The traditional pipeline when working with images stores in a clinical PACS
# implies:
# 
# - Connect to a XNAT database and request the images.
# - Convert images to NIfTI, and if possible to the BIDS format.
# - Process the images.
#
# This notebook illustrate these steps and it is intended to show how it can be
# simplified using [Clinica](https://www.clinica.run/).
#
# %% [markdown]
# 
# ## Connect to a PACS, the XNAT central and download images.
#
# For this example we use [XNAT central](https://www.xnat.org) and its Python
# client to download the full images. For this example, we use images available
# [here](https://central.xnat.org/app/action/DisplayItemAction/search_element/xnat%3AprojectData/search_field/xnat%3AprojectData.ID/search_value/OlgaKotelko)

# %%
import xnat

session = xnat.connect(
    "https://central.xnat.org",
    user="a3f9ac32-ed38-450e-8498-4a3d34bc1915",
    password="pHTpVxZVcZ7cVX0xJ0KN0hJGbWD0OAlo6tg0ILNc7KMdNdNAucnXpgMX7RLePXRV",
)
session.projects
# %%
olga_kotelko_project = session.projects["OlgaKotelko"]
olga_kotelko_project.subjects
# %% [markdown]
# Download images into a zip folder:

# %%
len(olga_kotelko_project.subjects)
experiment = olga_kotelko_project.experiments["AK_Mix_56_072412"]
# experiment = connection.create_object('/data/projects/$PROJECT_ID/experiments/$EXPERIMENT_ID')
# experiment = session.create_object('/data/xnat_central/archive/OlgaKotelko/arc001/AK_Mix_56_072412/')
# %%
experiment.scans["MPRAGE"]
experiment.scans["MPRAGE"].download("./dataset/mprage.zip")
# %%
session.disconnect()
#
# %% [markdown]
# Uncompress and visualize images
# %%
# TODO
# %% [markdown]
# ## Convert images to NIfTI 

# %% [markdown]
# ## Process images
# - A Pydra example ? Defacing ?

