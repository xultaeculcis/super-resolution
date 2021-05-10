from typing import Optional

import torch.nn as nn
from abc import abstractmethod

from PIL.Image import Image
from torch import Tensor
from torchvision import transforms


class SuperResolutionBaseModel(nn.Module):
    def __init__(self):
        super(SuperResolutionBaseModel, self).__init__()
        self.to_tensor = transforms.ToTensor()

    @abstractmethod
    def preprocess_input(self, lr_image: Image) -> Tensor:
        """
        Handle input image pre-processing like: normalization, resizing, tiling etc.

        :param lr_image: The LR image.
        :type lr_image: Image
        :return: The image tensor.
        :rtype: Tensor
        """
        pass

    @abstractmethod
    def postprocess_output(self, prediction: Tensor, lr_image: Optional[Image] = None) -> Image:
        """
        Handle prediction post-processing like: de-normalization, merging, masking etc.

        :param prediction: The network output.
        :type prediction: Tensor
        :param lr_image: Optional LR image.
        :type lr_image: Image
        :return: The PIL Image.
        :rtype: Image
        """
        pass
