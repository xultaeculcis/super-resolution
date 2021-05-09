# -*- coding: utf-8 -*-
import streamlit as st

from app.pages import consts


def usage_scenarios_page():
    st.title(consts.USAGES_PAGE_NAME)

    # ___________Usage Scenarios___________
    st.markdown("SR is popularly used in the following applications: ")

    # ___________Surveillance___________
    st.header("Surveillance")
    st.markdown(
        "To detect, identify, and perform facial recognition on low-resolution images obtained from "
        "security cameras."
    )
    st.image("./assets/use-cases/suspect-original.png")
    st.image("./assets/use-cases/suspect-enhanced.png")
    st.markdown(
        "[Source](https://www1.nyc.gov/site/nypd/services/see-say-something/crimestoppers.page)"
    )
    st.markdown(
        "Application of the SR techniques to enhance surveillance footage is the closest thing that we have to what "
        "we can see in the CSI TV Series :)"
    )

    # ___________Medical___________
    st.header("Medical Imagery")
    st.image("./assets/use-cases/medical.jpeg")
    st.markdown("[Source](https://www.biorxiv.org/content/10.1101/740548v2)")
    st.image("./assets/use-cases/medical2.png")
    st.markdown(
        "[Source](https://openaccess.thecvf.com/content_WACV_2020/papers/Wang_Enhanced_generative_adversarial_network_for_3D_brain_MRI_super-resolution_WACV_2020_paper.pdf)"  # noqa E501
    )
    st.markdown(
        "Medical: capturing high-resolution MRI images can be tricky when it comes to scan time, spatial coverage, "
        "and signal-to-noise ratio (SNR). Super resolution helps resolve this by generating high-resolution MRI from "
        "otherwise low-resolution MRI images."
    )

    # ___________Media___________
    st.header("Media")
    st.image("./assets/use-cases/media.png")
    st.markdown(
        "[Source](https://cvnote.ddlee.cc/2019/09/22/image-super-resolution-datasets)"
    )
    st.markdown(
        "Media: super resolution can be used to reduce server costs, as media can be sent at a lower resolution and "
        "upscaled on the fly. Figure above presents difference between LR and HR PIRM self-val images. "
        "On the left we have 4x downscaled images, and on the right the original HR images."
    )

    # ___________Real-World Super Resolution___________
    st.header("Real-World Super Resolution")
    st.image("./assets/use-cases/real-sr.png")
    st.image("./assets/use-cases/real-sr2.png")
    st.markdown("[Source](https://github.com/Tencent/Real-SR)")
    st.markdown(
        "Real-World Super Resolution: SR can be used to reduce artifacts and noise from real-world images. "
        "Basically you can enhance all of your selfies amd vacation pictures before uploading them to "
        "Facebook or Instagram :)"
    )

    # ___________DLSS___________
    st.header("Game optimization - DLSS")
    st.image("./assets/use-cases/dlss.jpeg")
    st.markdown("[Source](https://developer.nvidia.com/dlss)")
    st.markdown(
        "DLSS (an acronym for Deep Learning Super Sampling) is a deep learning neural network that uses the power of "
        "the NVIDIA RTX TensorCores to boost frame rates and generate sharp frames that approach or exceed native "
        "rendering. By tapping into a deep learning neural network, DLSS is able to combine anti-aliasing, "
        "feature enhancement, image sharpening and display scaling which traditional anti-aliasing solutions cannot. "
        "With this approach, DLSS delivers up to 2X greater performance with comparable image quality to full "
        "resolution native rendering. It gives you the performance headroom to maximize ray tracing settings and "
        "increase output resolution. DLSS is powered by dedicated AI processors on RTX GPUs called Tensor Cores."
    )

    # ___________In conjunction with other DL techniques___________
    st.header("In conjunction with other DL techniques")
    st.image("./assets/use-cases/sr-object-detection.png")
    st.markdown("[Source](https://arxiv.org/abs/1803.11316)")
    st.markdown(
        "Imagine that you have a bunch of data and want to do some object detection with it. However, the data is "
        "really low quality, perhaps from old or cheep video cameras. And when you try to apply your plain "
        "DL models they don't perform too well... You can boot their performance by first running your images through "
        "SR network."
    )
    st.markdown(
        "The other instance when you might want to apply SR to your images first is when the HR data "
        "collection is expensive. This is especially true for satellite imagery, where 1 sq. km of 30cm imagery can "
        "cost over $25. The cost of imagery with resolution of 1m is around $10 per sq. km. This means that, for "
        "a batch of 1000 sq. km you pay $10,000 and not $25,000 - huge cost savings for your company."
    )
