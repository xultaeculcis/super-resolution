# -*- coding: utf-8 -*-
import streamlit as st

from app.pages import consts


def sources_page():
    st.title(consts.SOURCES_PAGE_NAME)
    st.header("Main source of information")
    st.markdown(
        "* [Deep Learning for Image Super-Resolution: A Survey](https://arxiv.org/abs/1902.06068)"
    )
    st.markdown(
        "* [Image Super-Resolution: A Comprehensive Review](https://blog.paperspace.com/image-super-resolution/)"
    )
    st.markdown(
        "* [Deep Learning for Single Image Super-Resolution: A Brief Review](https://arxiv.org/abs/1808.03344)"
    )
    st.header("Memes")
    st.markdown("* [Meme Generator](https://imgflip.com/memegenerator)")
    st.markdown(
        "* [Reality is often disappointing](https://keepmeme.com/meme/reality-is-often-disappointing-thanos-meme)"
    )
    st.markdown(
        "* [Futurama - Enhance image](https://knowyourmeme.com/photos/996305-zoom-and-enhance)"
    )
    st.markdown(
        "* [CSI NY - We've Got the Killer](https://knowyourmeme.com/photos/995784-zoom-and-enhance)"
    )
    st.header("Architectures")
    st.markdown("* [SRCNN](https://arxiv.org/abs/1501.00092)")
    st.markdown("* [VDSR](https://arxiv.org/abs/1511.04587)")
    st.markdown("* [FSRCNN](https://arxiv.org/abs/1608.00367)")
    st.markdown("* [ESPCN](https://arxiv.org/abs/1609.05158)")
    st.markdown("* [EDSR](https://arxiv.org/abs/1707.02921)")
    st.markdown("* [MDSR](https://arxiv.org/abs/1707.02921)")
    st.markdown("* [CARN](https://arxiv.org/abs/1803.08664)")
    st.markdown(
        "* [BTSRN](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Fan_Balanced_Two-Stage_Residual_CVPR_2017_paper.pdf)"  # noqa E501
    )
    st.markdown("* [DRCN](https://arxiv.org/abs/1511.04491)")
    st.markdown(
        "* [DRRN](https://openaccess.thecvf.com/content_cvpr_2017/papers/Tai_Image_Super-Resolution_via_CVPR_2017_paper.pdf)"  # noqa E501
    )
    st.markdown("* [LAPSRN](https://arxiv.org/abs/1710.01992)")
    st.markdown("* [CMSC](https://arxiv.org/abs/1802.08808)")
    st.markdown(
        "* [IDN](https://openaccess.thecvf.com/content_cvpr_2018/papers/Hui_Fast_and_Accurate_CVPR_2018_paper.pdf)"
    )
    st.markdown(
        "* [SelNet](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Choi_A_Deep_Convolutional_CVPR_2017_paper.pdf)"  # noqa E501
    )
    st.markdown("* [RCAN](https://arxiv.org/abs/1807.02758)")
    st.markdown("* [SRGAN](https://arxiv.org/abs/1609.04802)")
    st.markdown("* [EnhanceNet](https://arxiv.org/abs/1612.07919v2)")
    st.markdown("* [ESRGAN](https://arxiv.org/abs/1809.00219)")

    st.header("Metrics & Loss Functions")
    st.markdown("* [SSIM](https://en.wikipedia.org/wiki/Structural_similarity)")
