# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts
from glob import glob
import os

def history_page():
    st.title(consts.HISTORY_PAGE_NAME)
    st.markdown("Original Image")

    original_files = sorted(glob("./assets/image-enhancement/original/*png"))
    lr_files = sorted(glob("./assets/image-enhancement/lr/*png"))

    for filter_name, description in [
        (
            "Nearest",
            "One of the simpler ways of increasing image size is nearest-neighbor interpolation, replacing every pixel "
            "with the nearest pixel in the output; for upscaling this means multiple pixels of the same color will be "
            "present. This can preserve sharp details in pixel art, but also introduce jaggedness in previously smooth "
            "images. 'Nearest' in nearest-neighbor doesn't have to be the mathematical nearest. One common "
            "implementation is to always round towards zero. Rounding this way produces fewer artifacts and is faster "
            "to calculate."
        ),
        (
            "Bilinear",
            "Bilinear interpolation works by interpolating pixel color values, introducing a continuous transition "
            "into the output even where the original material has discrete transitions. Although this is desirable "
            "for continuous-tone images, this algorithm reduces contrast (sharp edges) in a way that may be "
            "undesirable for line art. Bicubic interpolation yields substantially better results, with an increase "
            "in computational cost."
        ),
        (
            "Bicubic",
            "Bilinear interpolation works by interpolating pixel color values, introducing a continuous transition "
            "into the output even where the original material has discrete transitions. Although this is desirable for "
            "continuous-tone images, this algorithm reduces contrast (sharp edges) in a way that may be undesirable "
            "for line art. Bicubic interpolation yields substantially better results, with an increase in "
            "computational cost."
        ),
        (
            "Box",
            "One weakness of bilinear, bicubic and related algorithms is that they sample a specific number of pixels. "
            "When down scaling below a certain threshold, such as more than twice for all bi-sampling algorithms, the "
            "algorithms will sample non-adjacent pixels, which results in both losing data, and causes rough results. "
            "The trivial solution to this issue is box sampling, which is to consider the target pixel a box on the "
            "original image, and sample all pixels inside the box. This ensures that all input pixels contribute to "
            "the output. The major weakness of this algorithm is that it is hard to optimize."
        ),
        (
            "Lanczos",
            "Sinc resampling in theory provides the best possible reconstruction for a perfectly bandlimited signal. "
            "In practice, the assumptions behind sinc resampling are not completely met by real-world digital images. "
            "Lanczos resampling, an approximation to the sinc method, yields better results. Bicubic interpolation can "
            "be regarded as a computationally efficient approximation to Lanczos resampling."
        ),
    ]:
        st.markdown(f"### {filter_name}")
        st.markdown(description)

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.markdown("LR")
        with col2:
            st.markdown(filter_name)
        with col3:
            st.markdown("HR")

        for fname in original_files:
            basename = os.path.basename(fname)
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                st.image(f"./assets/image-enhancement/lr/LR-{basename}")
            with col2:
                st.image(f"./assets/image-enhancement/upscaled/{filter_name.upper()}-{basename}")
            with col3:
                st.image(f"./assets/image-enhancement/hr/HR-{basename}")
