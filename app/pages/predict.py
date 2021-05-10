# -*- coding: utf-8 -*-
import base64
from io import BytesIO

import streamlit as st
from PIL import Image

from app.pages import consts
from app.inference.model_configs import models, model_upscale_factors, model_versions
from app.inference.runner import InferenceRunner


def predict_page():
    st.title(consts.DEMO_PAGE_NAME)
    st.markdown("Here you can test the neural networks.")

    # ----------- Configure
    st.header("Configure")
    st.markdown(
        "Please select your run configuration first (testing network performance and predicting new results will "
        "depend on it):"
    )

    model_name = st.selectbox(
        label="Choose network architecture",
        options=[m.upper() for m in models],
        index=0,
    ).lower()

    model_scaling_factor = st.selectbox(
        label="Choose upscale factor",
        options=model_upscale_factors[model_name],
        index=0,
    )

    model_version = None
    if model_versions[model_name]:
        model_version = st.selectbox(
            label="Choose model version",
            options=model_versions[model_name],
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
        hr_img = Image.open(hr_upload)

        hr_w, hr_h = hr_img.size
        if hr_w > 512 or hr_h > 512:
            st.error(
                f"Uploaded image is too large. Max image resolution is capped at 512x512 px. "
                f"You uploaded {hr_w}x{hr_h} px."
            )

        else:
            runner = InferenceRunner(
                model_name=model_name,
                upscale_factor=int(model_scaling_factor.replace("x", "")),
                model_version=model_version,
            )
            lr, cubic, sr, results = runner.run_test(hr_img)
            col1, col2 = st.beta_columns(2)
            with col1:
                st.markdown("HR")
                st.image(hr_img)
            with col2:
                st.markdown("LR")
                st.image(lr)

            col1, col2 = st.beta_columns(2)
            with col1:
                st.markdown("Cubic")
                st.image(cubic)
                for k, v in results["cubic"].items():
                    st.markdown(f"{k}: {v:.4f}")
            with col2:
                st.markdown("SR")
                st.image(sr)
                for k, v in results[model_name].items():
                    st.markdown(f"{k}: {v:.4f}")

    # ----------- Predict new
    st.header("Predict new")
    lr_upload = st.file_uploader(
        label="Upload your LR image (max size: 1MB, max resolution: 512x512 px)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
    )
    if lr_upload:
        lr_image = Image.open(lr_upload)
        lr_w, lr_h = lr_image.size
        if lr_w > 512 or lr_h > 512:
            st.error(
                f"Uploaded image is too large. Max image resolution is capped at 512x512 px. "
                f"You uploaded {lr_w}x{lr_h} px."
            )

        else:
            runner = InferenceRunner(
                model_name=model_name,
                upscale_factor=int(model_scaling_factor.replace("x", "")),
                model_version=model_version,
            )
            sr = runner.run_inference(lr_image)

            def get_img_download_link(img):
                """Generates a link allowing the data from a given image to be downloaded"""
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/png;base64,{img_str}" download="sr_result.png">Download result</a>'
                return href

            col1, col2 = st.beta_columns(2)
            with col1:
                st.markdown("LR")
                st.image(lr_image)
            with col2:
                st.markdown("SR")
                st.image(sr)
                st.markdown(get_img_download_link(sr), unsafe_allow_html=True)
