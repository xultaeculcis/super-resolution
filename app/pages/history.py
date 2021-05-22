# -*- coding: utf-8 -*-
import streamlit as st
from pages import consts
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
        "However none of this work made its way into the standard textbooks on image processing [Pratt, "
        "1978; Gonzalez and Wintz, 1977; Rosenfeld and Kak, 1982] or computer graphics [Foley and van "
        "Dam, 1982] which were all produced around 1980. The exception to this is Newman and Sproull’s "
        "[1979] *“Principles of Interactive Computer Graphics”*, but even they only mention the subject in "
        "passing [ibid., p.265]. The image processing texts do spend time on image restoration, which is "
        "related to a priori knowledge reconstruction, but none on resampling."
    )
    st.markdown(
        "It was in the eighties that far more interest was paid to digital image resampling. The rush of publications "
        "was probably due to increased computer power and increased interest in raster displays; both for "
        "geometrical correction of digital images and for generation of realistic synthetic images. "
    )
    st.markdown(
        "Heckbert [1986] presented a good survey of texture mapping as it was to date. He built on this "
        "foundation in his masters thesis [Heckbert, 1989], which is a valuable reference for those working "
        "in texture mapping."
    )
    st.markdown(
        "The work on image resampling reached a milestone in 1990. In that year the first book [Wolberg, "
        "1990] was published on the subject and the new standard texts [Foley et al 1990; Pratt, 1991] "
        "included sections on image resampling and its related topics."
    )
    st.markdown(
        "*“Digital Image Warping”* by George Wolberg [1990] is the only existing book on digital image "
        "resampling. Prior to its publication the only source of information on image resampling was a "
        "myriad of articles scattered through technical journals and conference proceedings across half a "
        "dozen fields. Wolberg’s book draws much of this material into one place providing a *“conceptually "
        "unified, interdisciplinary survey of the field”* [Heckbert, 1991]."
    )
    st.markdown(
        "Wolberg’s book is not, however, the final word on image resampling. His specific aim was to "
        "emphasise the computational techniques involved rather than any theoretical framework [Wolberg, "
        "1991]. *“Digital Image Warping”* has its good points [McDonnell, 1991] and its bad [Heckbert, "
        "1991] but as the only available text it is a useful resource for the study of resampling (for a review "
        "of the book see Heckbert [1991]; the discussion sparked by this review may be found in Wolberg "
        "[1991], McDonnell [1991] and Heckbert [1991] - soruces provided on the **Sources** Page)."
    )
    st.markdown(
        "The most recent standard text, Foley, van Dam, Feiner and Hughes [1990] *“Computer Graphics: "
        "Principles and Practice”*, devotes some considerable space to image resampling and its related "
        "topics. Its predecessor [Foley and van Dam, 1982] made no mention at all of the subject. This "
        "reflects the change in emphasis in computer graphics from vector to raster graphics over the "
        "past decade. The raster display is now the most common *‘soft-copy’* output device [Sproull, "
        "1986; Fournier and Fussell, 1988], cheap raster displays having been developed in the mid "
        "70' as an offshoot of the contemporary television technology [Foley and van Dam, 1982]. "
        "Today it is true to say that *“with only a few specialised exceptions, line [vector] graphics has been "
        "subsumed by... raster graphics”* [Fiume, 1986, p.2]."
    )
    st.header("What is resampling?")
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

    # --------Resampling filters--------
    st.header("Comparison of resampling methods")
    st.image("./assets/image-enhancement/sampling-algo-comparison.png")
    st.markdown("[Source](https://en.wikipedia.org/wiki/Bicubic_interpolation)")

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
        "images. 'Nearest' in nearest-neighbor doesn't have to be the mathematical nearest. The nearest neighbor "
        "algorithm selects the value of the nearest point and does not consider the values of neighboring points "
        "at all, yielding a piecewise-constant interpolant. One common implementation is to always round towards zero. "
        "Rounding this way produces fewer artifacts and is faster to calculate. The diagonal lines of the images, "
        "tend to show the 'stairway' shape characteristic of nearest-neighbor interpolation. Other scaling methods "
        "are better at preserving smooth contours in the image.",
        "Spline interpolations are relatively fast, based on polynomial interpolation of order $n$ with $n-1$ "
        "continuous derivatives. Bilinear interpolation is one of the basic resampling techniques in computer vision "
        "and image processing, where it is also called bilinear filtering or bilinear texture mapping. "
        "Bilinear interpolation works by interpolating pixel color values, introducing a "
        "continuous transition into the output even where the original material has discrete transitions. "
        "Linear (or bilinear, in two dimensions) interpolation is typically good for changing the size of an image, but"
        " causes some undesirable softening of details and can still be somewhat jagged. Although this is desirable "
        "for continuous-tone images, this algorithm reduces contrast (sharp edges) in a way that may be undesirable "
        "for line art.",
        "In image processing, bicubic interpolation is often chosen over bilinear or nearest-neighbor interpolation "
        "in image resampling, when speed is not an issue. In contrast to bilinear interpolation, which only takes "
        "4 pixels (2×2) into account, bicubic interpolation considers 16 pixels (4×4). Images resampled with bicubic "
        "interpolation are smoother and have fewer interpolation artifacts.",
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

    # --------Metrics--------
    st.header("Metrics")
    st.markdown(
        "In this section we shall discuss the various metrics used to compare the performance of various models."
    )
    st.markdown(
        "1. **PSNR**: Peak Signal to Noise Ratio is the most common technique used to determine the quality of"
        " results. It can be calculated directly from the MSE using the formula below, where L is the maximum pixel "
        "value possible (255 for an 8-bit image)."
    )
    st.latex(r"PSNR = 10log_{10} (\frac{L^2}{MSE})")
    st.markdown(
        "2. **SSIM**: This metric is used to compare the perceptual quality of two images using the formula below, "
        "with the mean (μ), variance (σ), and correlation (c) of both images."
    )
    st.latex(
        r"SSIM(x, y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}"  # noqa E501
    )
    st.markdown("with:")
    st.markdown(r"* $x$ - the $HR$ image;")
    st.markdown(r"* $y$ - the $SR$ image;")
    st.markdown(r"* $\mu_x$ - the average of $x$;")
    st.markdown(r"* $\mu_y$ - the average of $y$;")
    st.markdown(r"* $\sigma_x^2$ - the variance of $x$;")
    st.markdown(r"* $\sigma_y^2$ - the variance of $y$;")
    st.markdown(r"* $\sigma_{xy}$ - the covariance of $x$ and $y$;")
    st.markdown(
        r"* $c_1 = (k_1L)^2, c_2 = (k_2L)^2$ - two variables to stabilize the division with weak denominator;"
    )
    st.markdown(
        r"* $L$ - the dynamic range of the pixel-values (typically this is $2^{\#bits\_per\_pixel} - 1$);"
    )
    st.markdown(r"* $k_1=0.01$ and $k_2=0.03$ by default.")
    st.markdown(
        "3. **MOS**: Mean Opinion Score is a manual way to determine the results of a model, where humans are asked to "
        "rate an image between 0 and 5. The results are aggregated and the average result is used as a metric."
    )
    st.markdown(
        "4. **MSE**: In Statistics, Mean Square Error (MSE) is defined as Mean or Average of the square of the "
        "difference between actual and estimated values."
    )
    st.latex(r"MSE = \frac{1}{N}\sum_{i=0}^{N} (HR_i - SR_i)^2")
    st.markdown(
        "5. **RMSE**: Root Mean Square Error (RMSE) is the standard deviation of the residuals (prediction errors). "
        "Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread "
        "out these residuals are. In other words, it tells you how concentrated the data is around the line of best "
        "fit. Root mean square error is commonly used in climatology, forecasting, and regression analysis to verify "
        "experimental results. "
    )
    st.latex(r"RMSE = \sqrt{MSE}")

    # --------Closeups--------
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

    st.markdown(
        "You can find some more scaling algorithms and their results here: "
        "[Comparison gallery of image scaling algorithms](https://en.wikipedia.org/wiki/Comparison_gallery_of_image_scaling_algorithms)"  # noqa E501
    )
