from typing import Optional

from PIL.Image import Image, fromarray
from torch import nn, Tensor
from torchvision import transforms
from torchvision.transforms import InterpolationMode

from inference.models.sr_base import SuperResolutionBaseModel
import numpy as np

from inference.utils import convert_rgb_to_ycbcr, convert_ycbcr_to_rgb


class SRCNN(SuperResolutionBaseModel):
    def __init__(self, num_channels=1, upscale_factor=2):
        super(SRCNN, self).__init__()
        self.conv1 = nn.Conv2d(num_channels, 64, kernel_size=9, padding=9 // 2)
        self.conv2 = nn.Conv2d(64, 32, kernel_size=5, padding=5 // 2)
        self.conv3 = nn.Conv2d(32, num_channels, kernel_size=5, padding=5 // 2)
        self.relu = nn.ReLU(inplace=True)
        self.upscale_factor = upscale_factor

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.conv3(x)
        return x

    def preprocess_input(self, lr_image: Image) -> Tensor:
        w, h = lr_image.size
        upscale = transforms.Resize(
            (h * self.upscale_factor, w * self.upscale_factor),
            interpolation=InterpolationMode.BICUBIC
        )

        image = np.array(upscale(lr_image)).astype(np.float32)
        ycbcr = convert_rgb_to_ycbcr(image)

        y = ycbcr[..., 0]
        y /= 255.

        return self.to_tensor(y).unsqueeze(0)

    def postprocess_output(self, prediction: Tensor, lr_image: Optional[Image] = None) -> Image:
        w, h = lr_image.size
        upscale = transforms.Resize(
            (h * self.upscale_factor, w * self.upscale_factor),
            interpolation=InterpolationMode.BICUBIC
        )
        image = np.array(upscale(lr_image)).astype(np.float32)

        ycbcr = convert_rgb_to_ycbcr(image)

        prediction = prediction.mul(255.0).cpu().numpy().squeeze(0).squeeze(0)

        output = np.array([prediction, ycbcr[..., 1], ycbcr[..., 2]]).transpose([1, 2, 0])
        output = np.clip(convert_ycbcr_to_rgb(output), 0.0, 255.0).astype(np.uint8)

        return fromarray(output)

