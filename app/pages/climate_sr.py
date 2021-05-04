# -*- coding: utf-8 -*-
import streamlit as st

from app.pages import consts


def climate_sr_page():
    # ______Climate Super-Resolution______
    st.title(consts.CLIMATE_SR_PAGE_NAME)
    st.image("./assets/climate-sr/world-clim-temperature.png")
    st.markdown(
        "On this page We'll present a novel usage of Super Resolution techniques that we had developed for the purpose "
        "of downscaling climate modelling data from [CRU-TS dataset](https://crudata.uea.ac.uk/cru/data/hrg/)."
    )
    st.markdown(
        "In climatology and geospatial sciences **\"downscaling\"** means *'to increase spatial resolution'* e.g., "
        "going from 1/2 deg. grid into 1/8 deg. grid (4x resolution increase). While in image "
        "processing world we would simply say **\"upscaling\"**. It might be confusing at first..."
    )

    # ______Problem definition______
    st.header("Problem definition")
    st.markdown(
        "The impacts of climate change are felt by most critical systems, such  as infrastructure, ecological systems, "
        "and power-plants. However, contemporary Earth System Models (ESM) are run at spatial resolutions too coarse "
        "for assessing effects this localized. Local scale projections can be obtained using statistical downscaling, "
        "a technique which uses historical climate observations to learn a low-resolution to high-resolution mapping. "
        "Depending on statistical modeling choices, downscaled projections have been shown to vary significantly in "
        "terms of accuracy and reliability. The spatio-temporal nature of the climate system motivates the adaptation "
        "of super-resolution image processing techniques to statistical downscaling."
    )
    st.markdown(
        "This Neural-Downscaling approach for downscaling precipitation and temperature data can be used to downscale "
        "from 1/2 degree (50km) to 1/8 degrees (12.5km) over the entirety of the globe, thus greatly reduce "
        "computational cost associated with generating CSMs."
    )

    # ______Implementation details______
    st.header("Implementation details")
    st.markdown("This section contains implementation details of proposed Neural-Downscaling approach.")

    # ______Dataset______
    st.markdown("### Dataset")
    st.markdown(
        "For example, in our application, we obtain climate data through the [WorldClim](https://www.worldclim.org/) "
        "dataset at a 1km spatial resolution which aggregates station observations to a grid with physical "
        "and topographical information. We then upscale the precipitation data to 1/8 degree (12.5 km) as our "
        "high-resolution observations. Following, we upscale further to 1/2 degree corresponding to a low-resolution "
        "climate (the same resolution as CRU-TS dataset). The goal is then to learn a mapping between our "
        "low-resolution and high-resolution datasets"
    )

    # ______Network______
    st.markdown("### Network")
    st.markdown(
        "Current solution is based on the simplest possible model - SRCNN. But more advanced architectures are "
        "being trained. The biggest hopes lay with GAN based architectures - especially ESRGAN."
    )

    # ______Data pre-processing______
    st.markdown("### Data pre-processing")
    st.markdown(
        r"The network takes as an input a batch of images of size $N \times C \times H \times W$, where:"
    )
    st.markdown("* $N$ - the number of training samples in the batch (batch size): in our case 64")
    st.markdown(
        "* $C$ - the number of channels: in our case this is 2 - one for climate data and one for elevation data"
    )
    st.markdown("* $H$ - the tile height: in our case 128")
    st.markdown("* $W$ - the tile width: in our case 128")
    st.markdown("TODO, datasets, variables, raster resizing, tile generation, normalization, augmentations,")

    # ______Training loop______
    st.markdown("### Training loop")
    st.markdown("TODO")

    # ______Tools and libs______
    st.markdown("### Tools and libs")
    st.markdown(
        "* [Python](https://www.python.org/): Python is an interpreted high-level general-purpose programming "
        "language. Currently the most popuar language for data science and geospatial big data processing enthusiasts "
        "and researchers."
    )
    st.markdown(
        "* [Anaconda](https://www.anaconda.com/): Anaconda is a distribution of the Python and R programming "
        "languages for scientific computing, that aims to simplify package management and deployment. The distribution "
        "includes data-science packages suitable for Windows, Linux, and macOS."
    )
    st.markdown(
        "* [Pytorch](https://pytorch.org/): An open source machine learning framework that accelerates the path from "
        "research prototyping to production deployment. Removes a lot of boilerplate code from your project. "
        "Automatically handles things like multiple GPUs, mixed-precision, distributed training, metrics "
        "implementation, logging, model checkpointing and visualization."
    )
    st.markdown(
        "* [Pytorch-Lightning](https://www.pytorchlightning.ai/): PyTorch Lightning is just organized PyTorch. "
        "Lightning disentangles PyTorch code to decouple the science from the engineering."
    )
    st.markdown(
        "* [xarray](http://xarray.pydata.org/en/stable/): (formerly xray) is an open source project and Python "
        "package that makes working with labelled multi-dimensional arrays simple, efficient, and fun!"
    )
    st.markdown(
        "* [Rasterio](https://rasterio.readthedocs.io/en/latest/): Geographic information systems use GeoTIFF and "
        "other formats to organize and store gridded raster datasets such as satellite imagery and terrain models. "
        "Rasterio reads and writes these formats and provides a Python API based on Numpy N-dimensional arrays "
        "and GeoJSON."
    )

    # ______Training visualizations______
    st.header("Training visualization")
    st.markdown("todo")
    st.image("./assets/climate-sr/training-progress.gif")
    st.markdown("todo")

    # ______Perceptual results______
    st.header("Perceptual results")
    st.markdown("todo")
    st.markdown("todo")
    st.markdown("todo")
