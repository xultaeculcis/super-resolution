# -*- coding: utf-8 -*-
import streamlit as st

from app.pages import consts


def climate_sr_page():
    st.title(consts.CLIMATE_SR_PAGE_NAME)
    st.markdown(
        "On this page I'll present a novel usage of Super Resolution techniques that I had developed for the purpose "
        "of downscaling climate modelling data from [CRU-TS dataset](https://crudata.uea.ac.uk/cru/data/hrg/)."
    )
    st.markdown(
        "In climatology and geospatial sciences **'downscaling'** means *'to increase spatial resolution'* e.g., "
        "going from 0.5 deg. grid into 0.125 deg. grid (4x resolution increase). While in image "
        "processing world we would simply say **'upscaling'**. It might be confusing at first..."
    )
    st.header("Problem definition")
    st.markdown(
        "The impacts of climate change are felt by most critical systems, such "
        "as infrastructure, ecological systems, and power-plants. However, "
        "contemporary Earth System Models (ESM) are run at spatial resolutions "
        "too coarse for assessing effects this localized. Local scale projections "
        "can be obtained using statistical downscaling, a technique "
        "which uses historical climate observations to learn a low-resolution "
        "to high-resolution mapping. Depending on statistical modeling "
        "choices, downscaled projections have been shown to vary significantly in "
        "terms of accuracy and reliability. The spatio-temporal nature "
        "of the climate system motivates the adaptation of super-resolution "
        "image processing techniques to statistical downscaling."
    )
    st.markdown("")
    st.header("Implementation details")
    st.markdown("todo")
    st.markdown("todo")
    st.header("Training visualization")
    st.markdown("todo")
    st.image("./assets/climate-sr/training-progress.gif")
    st.markdown("todo")
    st.header("Perceptual results")
    st.markdown("todo")
    st.markdown("todo")
    st.markdown("todo")
