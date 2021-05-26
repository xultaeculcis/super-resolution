# -*- coding: utf-8 -*-
import streamlit as st

from pages import consts


def sr_page():
    st.title(consts.SR_PAGE_NAME)

    # --------Image Super-Resolution--------
    st.header("Image Super-Resolution")
    st.markdown(
        "Low resolution images can be modeled from high resolution images using the below formula, where $D$ is the "
        "degradation function, $HR$ is the high resolution image, $LR$ is the low resolution image, and $σ$ is the "
        "noise."
    )
    st.latex(r"LR = D(HR; σ)")
    st.markdown(
        "The degradation parameters $D$ and $σ$ are unknown; only the high resolution image and the corresponding "
        "low resolution image are provided. The task of the neural network is to find the inverse function of "
        "degradation using just the $HR$ and $LR$ image data."
    )

    # --------Super-Resolution Methods and Techniques--------
    st.header("Super-Resolution Methods and Techniques")
    st.markdown(
        "There are many methods used to solve this task. We will cover the following:"
    )
    st.markdown("* Pre-Upsampling Super Resolution")
    st.markdown("* Post-Upsampling Super Resolution")
    st.markdown("* Residual Networks")
    st.markdown("* Multi-Stage Residual Networks")
    st.markdown("* Recursive Networks")
    st.markdown("* Progressive Reconstruction Networks")
    st.markdown("* Multi-Branch Networks")
    st.markdown("* Attention-Based Networks")
    st.markdown("* Generative Models")

    st.image("./assets/architectures/sr-hierarchy.png")
    st.markdown("[Source](https://arxiv.org/abs/1902.06068)")
    st.markdown("We'll look at several example algorithms for each.")

    # --------Pre-Upsampling Super Resolution--------
    st.header("Pre-Upsampling Super Resolution")
    st.markdown(
        "The methods under this bracket use traditional techniques – like bicubic interpolation and "
        "deep learning–to refine an upsampled image. The most popular method, SRCNN, was also the first to "
        "use deep learning, and has achieved impressive results."
    )
    # --------SRCNN--------
    st.markdown("### SRCNN")
    st.image("./assets/architectures/SRCNN.png")
    st.markdown("[Source](https://arxiv.org/abs/1501.00092)")
    st.markdown(
        "SRCNN is a simple CNN architecture consisting of three layers: one for patch extraction, "
        "non-linear mapping, and reconstruction. The patch extraction layer is used to extract dense patches "
        "from the input, and to represent them using convolutional filters. The non-linear mapping layer "
        "consists of 1×1 convolutional filters used to change the number of channels and add non-linearity. "
        "As you might have guessed, the final reconstruction layer reconstructs the high resolution image. "
    )
    st.markdown(
        "The MSE loss function is used to train the network, and PSNR (discussed in the Metrics section) "
        "is used to evaluate the results."
    )
    # --------VDSR--------
    st.markdown("### VDSR")
    st.image("./assets/architectures/VDSR.png")
    st.markdown("[Source](https://arxiv.org/abs/1511.04587)")
    st.markdown(
        "Very Deep Super Resolution (VDSR) is an improvement on SRCNN, with the addition of the following features:"
    )
    st.markdown(
        "* As the name signifies, a deep network with small 3×3 convolutional filters is used instead of a smaller "
        "network with large convolutional filters. This is based on the VGG architecture."
    )
    st.markdown(
        "* The network tries to learn the residual of the output image and the interpolated input, rather than "
        "learning the direct mapping (like SRCNN), as shown in the figure above. This simplifies the task. "
        "The initial low resolution image is added to the network output to get the final HR output."
    )
    st.markdown(
        "* Gradient clipping is used to train the deep network with higher learning rates."
    )

    # --------Post-Upsampling Super Resolution--------
    st.header("Post-Upsampling Super Resolution")
    st.markdown(
        "Since the feature extraction process in pre-upsampling SR occurs in the high resolution space, "
        "the computational power required is also on the higher end. Post-upsampling SR tries to solve this by doing "
        "feature extraction in the lower resolution space, then doing upsampling only at the end, therefore "
        "significantly reducing computation. Also, instead of using simple bicubic interpolation for upsampling, "
        "a learned upsampling in the form of deconvolution/sub-pixel convolution is used, thus making the network "
        "trainable end-to-end."
    )
    st.markdown("Let's discuss a few popular techniques following this structure.")

    # --------FSRCNN--------
    st.markdown("### FSRCNN")
    st.image("./assets/architectures/FSRCNN.png")
    st.markdown("[Source](https://arxiv.org/abs/1608.00367)")
    st.markdown(
        "As can be seen in the above figure, the major changes between SRCNN and FSRCNN are:"
    )
    st.markdown(
        "* There is no pre-processing or upsampling at the beginning. The feature extraction took place in the low "
        "resolution space."
    )
    st.markdown(
        "* A 1×1 convolution is used after the initial 5×5 convolution to reduce the number of channels, and hence "
        "lesser computation and memory, similar to how the Inception network is developed."
    )
    st.markdown(
        "* Multiple 3×3 convolutions are used, instead of having a big convolutional filter, similar to how the VGG "
        "network works by simplifying the architecture to reduce the number of parameters."
    )
    st.markdown(
        "* Upsampling is done by using a learned deconvolutional filter, thus improving the model."
    )
    st.markdown(
        "FSRCNN ultimately achieves better results than SRCNN, while also being faster."
    )

    # --------ESPCN--------
    st.markdown("### ESPCN")
    st.markdown(
        "ESPCN introduces the concept of sub-pixel convolution to replace the deconvolutional layer for upsampling. "
        "This solves two problems associated with it:"
    )
    st.markdown(
        "* Deconvolution happens in the high resolution space, and thus is more computationally expensive."
    )
    st.markdown(
        "* It resolves the checkerboard issue in deconvolution, which occurs due to the overlap operation of "
        "convolution (shown below)."
    )
    st.image("./assets/architectures/ESPCN1.png")
    st.markdown("[Source](https://arxiv.org/abs/1609.05158)")
    st.markdown(
        "Sub-pixel convolution works by converting depth to space, as seen in the figure below. Pixels from multiple "
        "channels in a low resolution image are rearranged to a single channel in a high resolution image. To give an "
        "example, an input image of size 5×5×4 can rearrange the pixels in the final four channels to a single "
        "channel, resulting in a 10×10 HR image."
    )
    st.image("./assets/architectures/ESPCN2.png")
    st.markdown("[Source](https://arxiv.org/abs/1609.05158)")

    # --------Residual Networks--------
    st.header("Residual Networks")

    # --------EDSR--------
    st.markdown("### EDSR")
    st.image("./assets/architectures/EDSR.png")
    st.markdown("[Source](https://arxiv.org/abs/1707.02921)")
    st.markdown(
        "The EDSR architecture is based on the SRResNet architecture, consisting of multiple residual blocks. "
        "The residual block in EDSR is shown above. The major difference from SRResNet is that the Batch Normalization "
        "layers are removed. The author states that BN normalizes the input, thus limiting the range of the network; "
        "removal of BN results in an improvement in accuracy. The BN layers also consume memory, and removing them "
        "leads to up to a 40% memory reduction, making the network training more efficient."
    )

    # --------MDSR--------
    st.markdown("### MDSR")
    st.markdown(
        "MDSR is an extension of EDSR, with multiple input and output modules that give corresponding resolution "
        "outputs at 2x, 3x, and 4x. At the beginning, the pre-processing modules for scale-specific input are present "
        "consisting of two residual blocks with 5×5 kernels. A large kernel is used for the pre-processing layers to "
        "keep the network shallow, while still achieving a high receptive field. At the end of the scale-specific "
        "pre-processing modules are the shared residual blocks, which is a common block for data of all resolutions. "
        "Finally, after the shared residual blocks are the scale-specific upsampling modules. Although the overall "
        "depth of MDSR is 5x compared to single-scale EDSR, the number of parameters are only 2.5x, and not 5x, due "
        "to the shared parameters. MDSR achieves comparable results to scale-specific EDSR, even though the network "
        "has fewer parameters than the scale-specific EDSR models combined."
    )

    # --------CARN--------
    st.markdown("### CARN")
    st.markdown(
        "In the paper Fast, Accurate, and Lightweight Super-Resolution with Cascading Residual Network, the authors "
        "have proposed the following advancements on top of a traditional residual network:"
    )
    st.markdown(
        "* A cascading mechanism at both the local and global level, to incorporate features from multiple layers and "
        "give the network the ability to receive more information."
    )
    st.markdown(
        "* In addition to CARN, a smaller CARN-M is proposed to have a lighter architecture, without much "
        "deterioration in results, with the help of recursive network architecture."
    )
    st.image("./assets/architectures/CARN.png")
    st.markdown("[Source](https://arxiv.org/abs/1803.08664)")
    st.markdown(
        "The global connections in CARN are visualized above. The culmination of each cascading block with a 1×1 "
        "convolution receives inputs from all the previous cascading blocks and the initial input, thus resulting "
        "in an effective transfer of information."
    )
    st.image("./assets/architectures/CARN2.png")
    st.markdown("[Source](https://arxiv.org/abs/1803.08664)")
    st.markdown(
        "Every residual block in a cascading block ends in a 1x1 convolution which has connections from all previous "
        "residual blocks along with the main input, similar to how global cascading works."
    )
    st.markdown(
        "The residual block in ResNet is replaced by a newly designed Residual-E block which is inspired from "
        "depthwise convolutions in MobileNet. Instead of depthwise convolutions, group convolutions are used, "
        "and the results show a decrease in 1.8-14x the number of computations used, depending on the group size."
    )
    st.markdown(
        "To further reduce the number of parameters, a shared residual block is used (recursive block), "
        "thus resulting in less number of parameters by up to three times the original number. As can be seen "
        "in (d) above, a recursive shared block helps in reducing the total number of parameters."
    )

    # --------Multi-Stage Residual Networks--------
    st.header("Multi-Stage Residual Networks")
    st.markdown(
        "To deal with the task of feature extraction separately in the low-resolution space and high-resolution "
        "space, a multi-stage design is considered in a few architectures to improve their performance. "
        "The first stage predicts the coarse features, while the later stage improves on it. Let's discuss "
        "an architecture involving one of these multi-stage networks."
    )

    # --------BTSRN--------
    st.markdown("### BTSRN")
    st.image("./assets/architectures/BTSRN.png")
    st.markdown(
        "[Source](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Fan_Balanced_Two-Stage_Residual_CVPR_2017_paper.pdf)"  # noqa E501
    )
    st.markdown(
        "As can be seen in the above figure, BTSRN consists of two stages: a low resolution (LR) stage and a "
        "high resolution (HR) stage. The LR stage consists of 6 residual blocks, whereas the HR stage contains 4 "
        "residual blocks. Convolution in the HR stage requires more computation than in the LR stage, as the input "
        "size is higher. The number of blocks in both the stages are determined in such a way as to achieve a "
        "trade-off between accuracy and performance."
    )
    st.markdown(
        "The output of the LR stage is upsampled before being sent to the HR stage. This is done by adding the "
        "outputs of the Deconvolution layer and Nearest Neighbor uspsampling."
    )
    st.markdown(
        "The authors propose a novel residual block named PConv, as seen in (d) in the figure above. The proposed "
        "block achieves a good trade-off between accuracy and performance, based on the results."
    )
    st.markdown(
        "Similar to EDSR, Batch Normalization is avoided to prevent re-centering and re-scaling, since it is "
        "found to be detrimental. This is due to the fact that super-resolution is a regression task, and thus "
        "target outputs are highly correlated with inputs' first-order statistics."
    )

    # --------Recursive Networks--------
    st.header("Recursive Networks")
    st.markdown(
        "Recursive networks employ shared network parameters in convolutional layers to reduce their memory "
        "footprint, as seen in CARN-M above. Let's discuss a few more architectures involving recursive units."
    )
    st.image("./assets/architectures/Recursive Networks.png")
    st.markdown("[Source](https://arxiv.org/abs/1808.03344)")

    # --------DRCN--------
    st.markdown("### DRCN")
    st.markdown(
        "Deep Recursive Convolutional Network (DRCN) involves applying the same convolution layer multiple times. "
        "As can be seen in the figure above, the convolutional layers in the residual block are shared."
    )
    st.image("./assets/architectures/DRCN.png")
    st.markdown("[Source](https://arxiv.org/abs/1511.04491)")
    st.markdown(
        "The outputs from all the intermediate shared convolutional blocks, along with the input, are sent to "
        "the reconstruction layer which generates the high resolution image using all of the inputs. Since there "
        "are multiple inputs used to generate the output, this architecture can be thought of as an ensemble "
        "of networks."
    )

    # --------DRRN--------
    st.markdown("### DRRN")
    st.markdown(
        "Deep Recursive Residual Network (DRRN) is an improvement over DRCN by having residual blocks in the network "
        "over simple convolutional layers. The parameters in every residual block are shared with other residual "
        "blocks, as can be seen in the image above."
    )
    st.image("./assets/architectures/DRRN.png")
    st.markdown("[Source](https://arxiv.org/abs/1808.03344)")
    st.markdown(
        "As you can see in the graph, DRRN outperforms SRCNN, ESPCN, VDSR, and DRCN, while having a comparable "
        "number of parameters."
    )

    # --------Progressive Reconstruction Networks--------
    st.header("Progressive Reconstruction Networks")
    st.markdown(
        "CNNs in general give outputs in a single shot, but getting a high resolution image with a big scale "
        "factor (say 8x) is a tough task for a neural network. To solve this, some network architectures increase "
        "the resolution of images in steps. Now let's discuss a few networks which follow this style."
    )

    # --------LAPSRN--------
    st.markdown("### LAPSRN")
    st.image("./assets/architectures/LAPSRN.png")
    st.markdown("[Source](https://arxiv.org/abs/1710.01992)")
    st.markdown(
        "LAPSRN, or MS-LAPSRN, consists of a Laplacian pyramid structure which can upscale images to 2x, 4x, "
        "and 8x using a step-by-step approach. As can be seen in the above figure, LAPSRN consists of multiple "
        "stages. The network consists of two branches: the Feature Extraction Branch and the Image Reconstruction "
        "Branch. Each iterative stage consists of a Feature Embedding Block and Feature Upsampling Block, as "
        "seen in the figure below. The input image is passed through a feature embedding layer to extract features "
        "in the low resolution space, which is then upsampled using transpose convolution. The output learned is a "
        "residual image which is added to the interpolated input to get the high resolution image. The output of the "
        "Feature Upsampling Block is also passed to the next stage, which is used for refining the high resolution "
        "output of this stage and scaling it to the next level. Since lower-resolution outputs are used in refining "
        "further stages, there is shared learning which helps the network to perform better."
    )
    st.image("./assets/architectures/LAPSRN2.png")
    st.markdown("[Source](https://arxiv.org/abs/1710.01992)")
    st.markdown(
        "To reduce the memory footprint of the network, the parameters in Feature Embedding, Feature Upsampling, "
        "etc. are shared across the stages recursively."
    )
    st.image("./assets/architectures/LAPSRN3.png")
    st.markdown("[Source](https://arxiv.org/abs/1710.01992)")
    st.markdown(
        "Within the feature embedding block, individual residual block consists of shared convolution parameters "
        "(shown in the figure above) to further reduce the number of parameters."
    )
    st.markdown(
        "The authors argued that since each LR input can have multiple HR representations, an L2 loss function "
        "produces a smoothed output over all representations, thus making the images not look sharp. "
        "To deal with this the Charbonnier loss function is used, which can handle outliers better."
    )

    # --------Multi-branch networks--------
    st.header("Multi-branch networks")
    st.markdown(
        "By now we've seen a trend: deeper networks give better results. But training deeper networks is "
        "tough due to the problem of information flow. Residual networks address this to an extent by using "
        "shortcut connections. Multi-branch networks work on improving information flow by having multiple "
        "branches through which information can pass, thus resulting in amalgamation of information from "
        "multiple receptive fields and hence better training. Let's discuss a few networks which employ "
        "this technique."
    )

    # --------CMSC--------
    st.markdown("### CMSC")
    st.markdown(
        "Like other super-resolution frameworks, the Cascaded Multi-Scale Cross-Network (CMSC) has a feature "
        "extraction layer, cascaded sub-nets, and a reconstruction layer–shown below."
    )
    st.image("./assets/architectures/CMSC.png")
    st.markdown("[Source](https://arxiv.org/abs/1802.08808)")
    st.markdown(
        "The cascaded sub-network consists of two branches, as can be seen in (b). Each branch has different sizes "
        "of filters, and hence results in a different receptive field. Fusion of information from different receptive "
        "fields across the module results in better information flow. Multiple blocks of MSC's are stacked one after "
        "another to gradually decrease the difference between the output and HR image iteratively. The outputs from "
        "all the blocks are passed together to a reconstruction block to get the final HR output."
    )

    # --------IDN--------
    st.markdown("### IDN")
    st.markdown(
        "Information Distillation Network (IDN) is proposed to achieve fast and accurate results for the task of "
        "super-resolution. Like other multi-branch networks, IDN utilizes the capability of multiple branches to "
        "improve the information flow in a deep network."
    )
    st.markdown(
        "The IDN architecture consists of FBlock to do feature extraction, multiple DBlocks, and RBlock to do "
        "transposed convolution to achieve learned upscaling. The contribution of the paper is in the DBlock, "
        "which consists of two units: the Enhancement Unit and Compression Unit."
    )
    st.image("./assets/architectures/IDN.png")
    st.markdown(
        "[Source](https://openaccess.thecvf.com/content_cvpr_2018/papers/Hui_Fast_and_Accurate_CVPR_2018_paper.pdf)"
    )
    st.markdown(
        "Enhancement unit's structure is shown in the figure above. Input is passed through three convolutional "
        "filters of size 3×3, and is then sliced. One part of the slice is concatenated with the initial input "
        "to pass via shortcut connection to the final layer. The remaining slice is passed through another set of "
        "convolutional filters of size 3×3. The final output is generated by summing up both the inputs and final "
        "layer. Having this kind of structure helps in capturing both the short-range information and the long-range "
        "information at the same time."
    )
    st.markdown(
        "The compression unit takes the output of the enhancement unit and passes it through a 1×1 convolutional "
        "filter to compress (or reduce) the number of channels."
    )

    # --------Attention-Based Networks--------
    st.header("Attention-Based Networks")
    st.markdown(
        "The networks discussed so far give equal importance to all spatial locations and channels. In general, "
        "giving selective attention to different regions in an image can give much better results. We shall now "
        "discuss few architectures which help in achieving this."
    )

    # --------SelNet--------
    st.markdown("### SelNet")
    st.image("./assets/architectures/SelNet.png")
    st.markdown(
        "[Source](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Choi_A_Deep_Convolutional_CVPR_2017_paper.pdf)"  # noqa E501
    )
    st.markdown(
        "SelNet proposes a novel Selection unit at the end of convolutional blocks which help to decide which "
        "information to pass on, selectively. A Selection Module consists of a ReLu activation followed by 1×1 "
        "convolution and sigmoid gating. A Selection Unit is the multiplication of a Selection Module and an "
        "identity connection."
    )
    st.markdown(
        "A sub-pixel layer (similar to ESPCN) is kept towards the end of the network to achieve learned upscaling. "
        "The network learns a residual HR image, which is then added to the interpolated input to get the final "
        "HR image."
    )

    # ________DRLN________
    st.markdown("### DRLN")
    st.image("./assets/architectures/DRLN.png")
    st.markdown("[Source](https://arxiv.org/abs/1906.12021v2)")  # noqa E501
    st.markdown(
        "Authors of Densely Residual Laplacian Super-Resolution present a compact and accurate super-resolution "
        "algorithm namely, Densely Residual Laplacian Network (DRLN). The proposed network employs cascading residual "
        "on the residual structure to allow the flow of low-frequency information to focus on learning high and "
        "mid-level features. In addition, deep supervision is achieved via the densely concatenated residual "
        "blocks settings, which also helps in learning from high-level complex features. Moreover, they propose "
        "Laplacian attention to model the crucial features to learn the inter and intra-level dependencies between "
        "the feature maps."
    )
    st.markdown(
        "This network is in top-5 on multiple benchmarks on "
        "[Papers with Code](https://paperswithcode.com/paper/densely-residual-laplacian-super-resolution) website. "
        "And currently holds the state-of-the-art title in multiple 8x upsampling benchmarks."
    )

    # --------RCAN--------
    st.markdown("### RCAN")
    st.markdown(
        "All through this article we have observed that having deeper networks improves performance. In order to "
        "train deeper networks, Residual Channel Attention Networks (RCAN) suggest RIR modules with Channel attention. "
        "Let's discuss these more in detail."
    )
    st.image("./assets/architectures/RCAN.png")
    st.markdown("[Source](https://arxiv.org/abs/1807.02758)")
    st.markdown(
        "The input in RCAN is passed through a single convolutional filter for feature extraction, which is then "
        "bypassed towards the final layer with a long skip connection. The long skip connection is added to carry "
        "the low frequency signals from the LR image while the main network (i.e RIR) focuses on capturing the "
        "high frequency information."
    )
    st.markdown(
        "RIR consists of multiple RG blocks, each having a structure shown in the above figure. Each RG block has "
        "multiple RCAB modules along with a skip connection, referred to as a short skip connection, to help transfer "
        "the low frequency signal."
    )
    st.image("./assets/architectures/RCAN2.png")
    st.markdown("[Source](https://arxiv.org/abs/1807.02758)")
    st.markdown(
        "RCAB has a structure (as shown above) comprised of a GAP module to achieve channel attention, similar to the "
        "Squeeze and Excite blocks in SqueezeNet. The channel-wise attention is multiplied with the output from the "
        "sigmoid gating function of a convolutional block. This output is then added to the shortcut input connection "
        "to get the final output value of a RCAB block."
    )

    # --------Generative Models--------
    st.header("Generative Models")
    st.markdown(
        "The networks discussed so far optimize the pixel difference between predicted and output HR images. Although "
        "this metric works fine, it is not ideal; humans don't distinguish images by pixel difference, but rather by "
        "perceptual quality. Generative models (or GANs) try to optimize the perceptual quality to produce images "
        "which are pleasant to the human eye. Finally, let's take a look at a few GAN-related architectures."
    )

    # --------SRGAN--------
    st.markdown("### SRGAN")
    st.image("./assets/architectures/SRGAN.png")
    st.markdown("[Source](https://arxiv.org/abs/1609.04802)")
    st.markdown(
        "SRGAN uses a GAN-based architecture to generate visually pleasing images. It uses the SRResnet network "
        "architecture as a backend, and employs a multi-task loss to refine the results. The loss consists of "
        "three terms:"
    )
    st.markdown("* MSE loss capturing pixel similarity")
    st.markdown(
        "* Perceptual similarity loss, which is used to capture high-level information by using a deep network"
    )
    st.markdown("* Adversarial loss from the discriminator")
    st.markdown(
        "Although the results obtained had comparatively lower PSNR values, the model achieved more MOS, i.e a "
        "better perceptual quality in the results."
    )

    # --------EnhanceNet--------
    st.markdown("### EnhanceNet")
    st.markdown(
        "EnhanceNet uses a Fully Convolutional Network with residual learning, which employs an extra term in the "
        "loss function to capture finer texture information. In addition to the above described losses in SRGAN, "
        "a texture loss similar to the one in Style Transfer is employed to capture the finer texture information."
    )
    st.image("./assets/architectures/EnhanceNet.png")
    st.markdown("[Source](https://arxiv.org/abs/1612.07919v22)")

    # --------ESRGAN--------
    st.markdown("### ESRGAN")
    st.markdown(
        "ESRGAN improves on top of SRGAN by adding a relativistic discriminator. The advantage is that the network "
        "is trained not only to tell which image is true or fake, but also to make real images look less real "
        "compared to the generated images, thus helping to fool the discriminator. Batch normalization in SRGAN is "
        "also removed, and Dense Blocks (inspired from DenseNet) are used for better information flow. "
        "These Dense Blocks are called RRDB."
    )
    st.image("./assets/architectures/ESRGAN.png")
    st.markdown("[Source](https://arxiv.org/abs/1809.00219)")
    st.markdown("Additionally authors propose to combine the two models:")
    st.markdown("* One trained strictly for PSNR,")
    st.markdown("* And one trained with GAN training.")
    st.markdown(
        "This approach allows them to fluently adjust output of the network. The authors won PIRM2018-SR "
        "Challenge thanks to proposed architecture."
    )

    # --------Datasets--------
    st.header("Datasets")
    st.markdown(
        "The following are some of the common datasets used to train super-resolution networks. "
    )
    st.markdown(
        "* [**DIV2K**](https://data.vision.ee.ethz.ch/cvl/DIV2K/):  800 train, 100 validation, and 100 test. 2K "
        "resolution images are provided, including both high and low resolution images with 2x, 3x, and 4x downscaling "
        "factors. Proposed in the NTIRE17 challenge. "
    )
    st.markdown(
        "* [**Flickr2K**](https://cvnote.ddlee.cc/2019/09/22/image-super-resolution-datasets): 2650 2K images from "
        "FLICKR."
    )
    st.markdown(
        "* [**Waterloo**](https://ece.uwaterloo.ca/~k29ma/exploration/): The Waterloo Exploration Database contains "
        "4,744 pristine natural images and 94,880 distorted "
        "images created from them. "
    )
    st.markdown(
        "* [**NTIRE 2020 - Real-World SR Challenge**](https://competitions.codalab.org/competitions/22220#learn_the_details): "  # noqa E501
        "A large dataset of Image Processing Artifacts (IPA) derived from Flickr2K and DIV2K of images with a large "
        "diversity of contents. The dataset contains images from the source domain of the input images and images "
        "defining a target domain. The target domain images are important, the super-resolved output images should "
        "belong to the target domain."
    )
    st.markdown(
        "* And many more - many of which are available "
        "[HERE](https://cvnote.ddlee.cc/2019/09/22/image-super-resolution-datasets)"
    )

    # --------Loss Functions--------
    st.header("Loss Functions")
    st.markdown(
        "In this section we shall discuss various loss functions which can be used to train the networks."
    )
    st.markdown(
        "* **Pixel Loss**: This is the most simple and common type of loss function used in training super-resolution "
        "networks. L2, L1, or some difference metric is used to evaluate the model. Training with pixel loss optimizes "
        "PSNR, but doesn't directly optimize the perceptual quality, and hence generates images which might not be "
        "pleasing to the human eye."
    )
    st.markdown(
        "* **Perceptual Loss**: Perceptual loss tries to match the high-level features in a generated image with "
        "a given HR output image. This is achieved by taking a pre-trained network, like VGG, and using the difference "
        "of feature outputs between predicted and output images as loss. This loss function is introduced in SRGAN."
    )
    st.markdown(
        "* **Charbonnier Loss**: This loss function is used in LapSRN instead of the generic L2 loss. The results show "
        "that Charbonnier loss deals better with outliers and produces sharper images compared to those generated with "
        "L2 loss, which are generally smoother."
    )
    st.markdown(
        "* **Texture Loss**: Introduced in EnhanceNet, this loss function tries to optimize the Gram matrix of feature "
        "outputs inspired by the Style Transfer loss function. This loss function trains the network to capture the "
        "texture information in a HR image."
    )
    st.markdown(
        "* **Adversarial Loss**: Used in all GAN-related architectures, adversarial loss helps in fooling the "
        "discriminator and generally produces images which have better perceptual quality. ESRGAN adds an extra "
        "variant of this by using the relativistic discriminator, and thus instructing the network not only to make "
        "fake images more real, but also to make real images look more fake."
    )

    # --------SOTA--------
    st.header("What are the best models?")
    st.markdown(
        "There is no definitive answer to that question. The model with the best PSNR might not have the best "
        "perceptual quality. And the model with the best perceptual quality might be too slow to be used in "
        "real-time applications. Choosing the model that suits your meeds the best might be a hard task. "
        "But thankfully there are sites that aggreate benchmark results from published scientific papers for us. "
        "You can check current state-of-the-art models by visiting "
        "[Papers with Code](https://paperswithcode.com/task/image-super-resolution) website."
    )
    st.image("./assets/architectures/papers-with-code-sota.png")

    # --------Summary--------
    st.header("Summary - what is it all for?")
    st.markdown(
        "That's all awesome, but is this SR thing only good for upscaling photos for my FB page? "
        "And if it is - why should I care?"
    )
    st.image("./assets/memes/bender-why-should-i-care-meme.jpeg")
