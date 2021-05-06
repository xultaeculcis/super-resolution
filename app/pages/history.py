# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts
from glob import glob
import os


def history_page():
    st.title(consts.HISTORY_PAGE_NAME)
    st.header("Early stages of image enhancement")
    st.markdown("TODO some history")

    st.header("Comparison of resampling filters")

    original_files = sorted(glob("./assets/image-enhancement/original/*png"))

    filter_names = [
        "Nearest",
        "Bilinear",
        "Bicubic",
        "Box",
        "Hamming",
        "Lanczos",
    ]
    descriptions = [
        "One of the simpler ways of increasing image size is nearest-neighbor interpolation, replacing every pixel "
        "with the nearest pixel in the output; for upscaling this means multiple pixels of the same color will be "
        "present. This can preserve sharp details in pixel art, but also introduce jaggedness in previously smooth "
        "images. 'Nearest' in nearest-neighbor doesn't have to be the mathematical nearest. One common "
        "implementation is to always round towards zero. Rounding this way produces fewer artifacts and is faster "
        "to calculate.",
        "Spline interpolations are relatively fast, based on polynomial interpolation of order $n$ with $n-1$ "
        "continuous derivatives. Bilinear interpolation works by interpolating pixel color values, introducing a "
        "continuous transition into the output even where the original material has discrete transitions. "
        "Although this is desirable for continuous-tone images, this algorithm reduces contrast (sharp edges) in a "
        "way that may be undesirable for line art. Bicubic interpolation yields substantially better results, with "
        "an increase in computational cost.",
        "Bilinear interpolation works by interpolating pixel color values, introducing a continuous transition "
        "into the output even where the original material has discrete transitions. Although this is desirable for "
        "continuous-tone images, this algorithm reduces contrast (sharp edges) in a way that may be undesirable "
        "for line art. Bicubic interpolation yields substantially better results, with an increase in "
        "computational cost.",
        "One weakness of bilinear, bicubic and related algorithms is that they sample a specific number of pixels. "
        "When down scaling below a certain threshold, such as more than twice for all bi-sampling algorithms, the "
        "algorithms will sample non-adjacent pixels, which results in both losing data, and causes rough results. "
        "The trivial solution to this issue is box sampling, which is to consider the target pixel a box on the "
        "original image, and sample all pixels inside the box. This ensures that all input pixels contribute to "
        "the output. The major weakness of this algorithm is that it is hard to optimize.",
        "Windowed sinc interpolations give ideal resamplings regularized by windows of the form ${window(x/(2r))}$ or "
        "${window(x/(2r),\\alpha)}$. Sinc resampling in theory provides the best possible reconstruction for a "
        "perfectly bandlimited signal. In practice, the assumptions behind sinc resampling are not completely met by "
        "real-world digital images. Hamming resampling technique is one of many examples of sinc methods.",
        "Lanczos resampling, an approximation to the sinc method, yields better results. Bicubic interpolation can "
        "be regarded as a computationally efficient approximation to Lanczos resampling.",
    ]

    for filter_name, description in zip(filter_names, descriptions):
        st.markdown(f"### {filter_name}")
        st.markdown(description)

    st.image("./assets/image-enhancement/upscaled/comparison_fig.png")

    st.header("Closeups")
    st.markdown("If you want to see the individual files here they are:")

    cols = st.beta_columns(9)

    col_names = ["Original", "HR", "LR"] + filter_names
    for col, name in zip(cols, col_names):
        with col:
            st.markdown(name)

    for fname in original_files:
        basename = os.path.basename(fname)
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.beta_columns(9)
        cols = [col4, col5, col6, col7, col8, col9]

        with col1:
            st.image(fname)
        with col2:
            st.image(f"./assets/image-enhancement/hr/HR-{basename}")
        with col3:
            st.image(f"./assets/image-enhancement/lr/LR-{basename}")

        for filter_name, column in zip(filter_names, cols):
            with column:
                st.image(
                    f"./assets/image-enhancement/upscaled/{filter_name.upper()}-{basename}"
                )
