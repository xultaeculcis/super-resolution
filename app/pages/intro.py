# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts


def intro_page():
    st.title(consts.INTRO_PAGE_NAME)

    st.header("What is Super Resolution?")
    st.markdown(
        "**Super-resolution imaging (SR)** is a class of techniques that enhance (increase) the resolution of an image "
        "from low-resolution (**LR**) to high (**HR**). "
    )
    st.markdown(
        "Deep learning (**DL**) techniques have been fairly successful in solving the problem of image and video "
        "super-resolution. This app provides theory involved, various techniques used, loss "
        "functions, metrics, and relevant datasets. You can also run the code of the most popular models by going "
        "into the Demo page of this application."
    )

    st.header("Expectations", "expectations")
    st.markdown(
        "So, it sounds kinda like what they do in this CSI MI/NY/LA (...) TV Series... Am I right?"
    )
    st.image("./assets/memes/csi-ny-enhance-meme.jpg")
    st.audio("./assets/memes/YEAAAAAAAAAAAAAH.mp3")

    st.header("Reality", "reality")
    st.markdown(
        "Well... In reality the image just does not have enough spatial information to recreate such details from "
        "low resolution image... Anything that goes beyond applying classic filters means that the SR system "
        "*hallucinates* new pixels. This is especially true with Deep Learning based SR techniques."
    )
    st.image("./assets/memes/enhance-futurama-meme.jpg")
    st.image("./assets/memes/thanos-reality-is-often-disappointing-meme.jpeg")
