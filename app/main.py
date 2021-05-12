# -*- coding: utf-8 -*-
import streamlit as st
from pages import (
    history_page,
    predict_page,
    climate_sr_page,
    sr_page,
    intro_page,
    sources_page,
    usage_scenarios_page,
    consts,
)
import logging
logging.basicConfig(level=logging.INFO)


st.set_page_config(
    page_title="Super Resolution",
    page_icon="./assets/icon.png",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Navigation")
method = st.sidebar.radio(label="Choose page", options=consts.PAGE_NAMES)


if method == consts.INTRO_PAGE_NAME:
    intro_page()
elif method == consts.HISTORY_PAGE_NAME:
    history_page()
elif method == consts.SR_PAGE_NAME:
    sr_page()
elif method == consts.USAGES_PAGE_NAME:
    usage_scenarios_page()
elif method == consts.CLIMATE_SR_PAGE_NAME:
    climate_sr_page()
elif method == consts.DEMO_PAGE_NAME:
    predict_page()
else:
    sources_page()
