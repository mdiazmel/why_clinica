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
# # The classic way of asking the PACS for image and processing
# Steps:
# - Connect to a XNAT database and download images
# - Convert images to NifTY if possible BIDS format
# - Test a pipeline pydra
#
# %% [markdown]
# ## Connect to a PACS, the XNAT central and download images.
#
# For this example we use [XNAT central](https://www.xnat.org) and its Python
# client to download full T1 images:

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
# %%
