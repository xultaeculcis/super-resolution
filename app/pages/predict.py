# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts


def predict_page():
    st.title(consts.DEMO_PAGE_NAME)
    st.markdown("Here you can test the neural networks.")

    # ----------- Configure
    st.header("Configure")
    st.markdown(
        "Please select your run configuration first (testing network performance and predicting new results will "
        "depend on it):"
    )

    srcnn = "SRCNN"
    srgan = "SRGAN"
    esrgan = "ESRGAN"
    drln = "DRLN"
    rcan = "RCAN"

    models = [srcnn, srgan, esrgan, drln, rcan]
    model_upscale_factors = {
        srcnn: ["2x", "4x"],
        srgan: ["2x", "4x"],
        esrgan: ["2x", "4x", "8x"],
        drln: ["2x", "4x", "8x", "16x"],
        rcan: ["2x", "4x"],
    }
    model_versions = {
        srcnn: ["v1"],
        srgan: ["v1"],
        esrgan: ["psnr-oriented", "perceptual-oriented", "mixed"],
        drln: ["v1"],
        rcan: ["v1"],
    }

    model = st.selectbox(
        label="Choose network architecture",
        options=models,
        index=0,
    )

    _ = st.selectbox(
        label="Choose upscale factor",
        options=model_upscale_factors[model],
        index=0,
    )

    _ = st.selectbox(
        label="Choose model version",
        options=model_versions[model],
        index=0,
    )

    # ----------- Test performance
    st.header("Test performance")
    hr_upload = st.file_uploader(
        label="Upload your HR image (max size: 1MB, max resolution: 512x512 px)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
    )
    if hr_upload:
        st.markdown("This is a summary of the network performance:")
        st.markdown("TODO: Plot results: HR, LR, Cubic, SR")

    # ----------- Predict new
    st.header("Predict new")
    lr_upload = st.file_uploader(
        label="Upload your LR image (max size: 1MB, max resolution: 512x512 px)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
    )
    if lr_upload:
        st.markdown("TODO: Display download button")
