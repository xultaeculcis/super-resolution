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
        "going from 1/2° grid into 1/8° grid (4x resolution increase). While in image processing world we would "
        'simply say **"upscaling"**. It might be confusing at first...'
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
        "from 1/2° (50 km) to 1/8° (12.5 km) over the entirety of the globe, thus greatly reduce computational cost "
        "associated with generating CSMs."
    )

    # ______Implementation details______
    st.header("Implementation details")
    st.markdown(
        "This section contains implementation details of proposed Neural-Downscaling approach."
    )

    # ______Dataset______
    st.markdown("### Dataset")
    st.markdown("We used 2 datasets:")
    st.markdown(
        "* [WorldClim](https://www.worldclim.org/) - WorldClim is a database of high spatial resolution global weather "
        "and climate data. These data can be used for mapping and spatial modeling. The data are provided for use in "
        "research and related activities. Historical monthly weather data for 1960-2018. The variables available are "
        "average minimum temperature (°C), average maximum temperature (°C) and total precipitation (mm). The spatial "
        "resolution is 2.5 minutes (0.0417°, ~21 km2). The WorldClim also provides elevation dataset (meters above "
        "mean sea level)."
    )
    st.markdown(
        "* [CRU-TS](https://crudata.uea.ac.uk/cru/data/hrg/) - The CRU TS v 4.04 dataset was developed and has been "
        "subsequently updated, improved and maintained with support from a number of funders, principally the UK's "
        "Natural Environment Research Council (NERC) and the US Department of Energy. Coverage: the period of "
        "1901-2019, of land areas (excluding Antarctica) at 0.5° resolution. Variables: average minimum temperature "
        "(°C), average average temperature (°C), average maximum temperature (°C) and precipitation (mm)."
    )
    st.markdown(
        "For example, in our application, we obtain climate data through the [WorldClim](https://www.worldclim.org/) "
        "dataset at a 1 km spatial resolution which aggregates station observations to a grid with physical "
        "and topographical information. We then upscale the precipitation data to 1/8° (12.5 km) as our "
        "high-resolution observations. Following, we upscale further to 1/2° corresponding to a low-resolution "
        "climate (the same resolution as CRU-TS dataset). The goal is then to learn a mapping between our "
        "low-resolution and high-resolution datasets."
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
    st.markdown(
        "* $N$ - the number of training samples in the batch (batch size): in our case 64"
    )
    st.markdown(
        "* $C$ - the number of channels: in our case this is 2 - one for climate data and one for elevation data"
    )
    st.markdown("* $H$ - the tile height: in our case 128")
    st.markdown("* $W$ - the tile width: in our case 128")
    st.markdown(
        "Prior to training, the data was pre-processed by resizing WorldClim dataset to target HR resolution of 1/8°. "
        "After resizing tile generation was performed. Tiles of size 128 $\\times$ 128 were generated using `Rasterio`"
        " and `Dask`. "
    )
    st.markdown(
        "While training each tile is normalized to fit in range [0;1] using prior knowledge of min and max values from "
        "the parent raster. LR images are generated from HR source images by resizing from 128 $\\times$ 128 "
        "to 32 $\\times$ 32 and then agiain resizing to 128 $\\times$ 128 nearest-neighbour interpolation. "
        "Random vertical, horizontal flips and 90 rotations are applied at training time. This makes the network to "
        "become spatially ignorant to tile geo-location."
    )

    # ______Training loop______
    st.markdown("### Training loop")
    st.markdown(
        "When training tiles of particular variable are concatenated with elevation data for that extent. The network "
        "is trained with standard training scheme with following configuration:"
    )
    st.markdown("* Loss function: L2 Loss")
    st.markdown("* Batch size: 64")
    st.markdown("* Max learning rate: 1e-4")
    st.markdown("* Optimizer: Adam (with default parameters)")
    st.markdown(
        """* LR Scheduler: OneCycle with:
    * `pct_start: 0.05`
    * `div_factor: 2.0`
    * `final_div_factor: 1e2`"""
    )
    st.markdown("* Downscaling factor: 4x")
    st.markdown("* HR image size: 128x128")
    st.markdown("* LR image size: 32x32")
    st.markdown("* Train years: 1961-1999")
    st.markdown("* Validation years: 2000-2005")
    st.markdown("* Test years: 2006-2019")
    st.markdown("* Main performance metric: $RMSE$")
    st.markdown(
        """* Helper metrics:
    * $MAE$
    * $MSE$
    * $PSNR$
    * $SSIM$
    * denormalized $MAE$
    * denormalized $MSE$
    * denormalized $RMSE$
    * denormalized $R^2$
    """
    )

    # ______Tools and libs______
    st.markdown("### Tools and libs")
    st.markdown(
        "* [Python](https://www.python.org/): Python is an interpreted high-level general-purpose programming "
        "language. Currently the most popular language for data science and geospatial big data processing enthusiasts "
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
    st.markdown(
        "* [Dask](https://dask.org/): Dask is an open source library for parallel computing written in Python. "
        "Originally developed by Matthew Rocklin, Dask is a community project maintained and sponsored by developers "
        "and organizations."
    )

    # ______Training visualizations______
    st.header("Training visualization and monitoring")
    st.markdown(
        "Below you can see training progress visualization. Please note on how with each epoch the results become "
        "sharper and more visually pleasing."
    )
    epoch = st.slider("Epoch:", 1, 30, 1)
    st.image(
        f"./assets/climate-sr/training_progress/sr-gen-pre-training-epoch={epoch-1}.png"
    )

    st.markdown(
        "For training monitoring a tool called Tensorboard was used. It comes configured out of the box with Lightning."
    )
    st.image("./assets/climate-sr/tensorboard.png")
    st.image("./assets/climate-sr/tensorboard2.png")

    # ______Perceptual results______
    st.header("Perceptual results")
    st.markdown("Below you can see the network inference results.")

    variable_names = [
        "Minimum temperature",
        "Average temperature",
        "Maximum temperature",
        "Total precipitation",
    ]
    variable_codes = ["tmn", "tmp", "tmx", "pre"]
    variable_to_code_mapping = dict(list(zip(variable_names, variable_codes)))
    var = st.selectbox(
        label="Select climate variable:", options=variable_names, index=0
    )
    var = variable_to_code_mapping[var]

    col1, col2 = st.beta_columns(2)

    with col1:
        st.markdown(f"LR input raster from CRU-TS ({var}): ")
        # st.image(f"./assets/climate-sr/results/{var}/cruts-{var}-2018-06-16.tif")
        st.image("./assets/climate-sr/world-clim-temperature.png")
    with col2:
        st.markdown("HR output raster from the network:")
        # st.image(f"./assets/climate-sr/results/{var}/cruts-{var}-2018-06-16.tif")
        st.image("./assets/climate-sr/world-clim-temperature.png")
