# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import consts
from glob import glob
import os


def history_page():
    st.title(consts.HISTORY_PAGE_NAME)
    st.header("Early stages of image enhancement")
    st.markdown(
        "The text in this section comes from this [source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-261.pdf)."
    )
    st.markdown(
        "Digital image resampling occupies a small but important place in the fields of image processing and computer "
        "graphics. In the most basic terms, resampling is the process of geometrically transforming digital images. "
    )
    st.markdown(
        "Digital image resampling has its beginnings in the early ’70s. Catmull [1974] was the first in the field of "
        "computer graphics to work on texture mapping, when he discovered a way to map images onto curved surfaces. "
        "Rifman, McKinnon, and Bernstein [Keys, 1981; Park and Schowengerdt, 1983] did some of the first work on "
        "resampling for correction of remotely sensed image data (satellite imagery) around the same time."
    )
    st.markdown(
        "Resampling finds uses in many fields. It is usually a step in a larger process, seldom an end in itself and "
        "is most often viewed as a means to an end. In computer graphics resampling allows texture to be applied to "
        "surfaces in computer generated imagery, without the need to explicitly model the texture. In medical and "
        "remotely sensed imagery it allows an image to be registered with some standard co-ordinate system, be it "
        "another image, a map, or some other reference. This is primarily done to prepare for further processing."
    )
    st.markdown(
        "Resampling is essentially a mathematical operation mapping one collection of numbers into another. "
        "The important point here is that what is seen by a human to be the input to and output from the resampling "
        "process are continuous representations of the underlying discrete images. There are many different ways of "
        "reconstructing a continuous image from a discrete one."
    )
    st.markdown(
        "What's a discrete and what's a continuous image? Continuous images have a real intensity at every point in "
        "the real plane. The image that is presented to a human eye or to a video camera, before any processing is "
        "done to it, is a continuous image. Discrete images only have intensity values at a set of discrete points and "
        "these intensities are drawn from a set of discrete values. The image stored in a computer display’s frame "
        "buffer is a discrete image. The discrete values are often called ‘pels’ or ‘pixels’ (contractions of "
        "'picture elements')."
    )
    st.markdown("Various practical uses of image resampling are:")
    st.markdown("* distortion compensation of optical systems.")
    st.markdown("* registration to some standard projection.")
    st.markdown(
        "* registration of images from different sources with one another; for example registering the different bands "
        "of a satellite image with one another for further processing"
    )
    st.markdown(
        "* registering images for time-evolution analysis. A good example of this is recorded by Herbin et al [1989] "
        "and Venot et al [1988] where time-evolution analysis is used to track the healing of lesions over periods of "
        "weeks or months."
    )
    st.markdown("* geographical mapping; changing from one projection to another.")
    st.markdown(
        "* photomosaicing; producing one image from many smaller images. This is often used to build up a picture of "
        "the surface of a planet from many photographs of parts of the planet’s surface."
    )
    st.markdown("* geometrical normalisation for image analysis.")
    st.markdown(
        "* television and movie special effects. Warping effects are commonplace in certain types of television "
        "production; often being used to enhance the transition between scenes. They are also used by the movie "
        "industry to generate special effects."
        ""
    )
    st.markdown(
        "* texture mapping; a technique much used in computer graphics. It involves taking an image and applying it to "
        "a surface to control the shading of that surface in some way."
    )

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

    selected_file = st.selectbox(
        label="Select file",
        options=[os.path.basename(fp).replace(".png", "") for fp in original_files],
        index=0,
    )

    cols = st.beta_columns(9)

    col_names = ["Original", "HR", "LR"] + filter_names
    for col, name in zip(cols, col_names):
        with col:
            st.markdown(name)

    if selected_file:
        basename = selected_file + ".png"
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.beta_columns(9)
        cols = [col4, col5, col6, col7, col8, col9]

        with col1:
            st.image(os.path.join("./assets/image-enhancement/original", basename))
        with col2:
            st.image(f"./assets/image-enhancement/hr/HR-{basename}")
        with col3:
            st.image(f"./assets/image-enhancement/lr/LR-{basename}")

        for filter_name, column in zip(filter_names, cols):
            with column:
                st.image(
                    f"./assets/image-enhancement/upscaled/{filter_name.upper()}-{basename}"
                )
