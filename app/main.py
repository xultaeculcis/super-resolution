# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import (
    history_page,
    predict_page,
    climate_sr_page,
    sr_page,
    intro_page,
    consts,
)


st.set_page_config(
    page_title="Super Resolution",
    page_icon="./assets/icon.png",
    layout="wide",
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
elif method == consts.CLIMATE_SR_PAGE_NAME:
    climate_sr_page()
else:
    predict_page()
