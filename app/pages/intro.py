# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts


def intro_page():
    st.title(consts.INTRO_PAGE_NAME)
