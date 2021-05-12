from typing import Dict, Tuple

import numpy as np
import torch
from PIL.Image import Image, fromarray
from torch import Tensor
from torchvision import transforms
from torchmetrics import PSNR, SSIM, MeanAbsoluteError, MeanSquaredError

from inference.loader import load_model


class InferenceRunner:
    def __init__(self, model_name, upscale_factor, model_version=None):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model_name = model_name
        self.upscale_factor = upscale_factor
        self.model_version = model_version
        self.model = load_model(model_name, upscale_factor, model_version).to(self.device)

        self.tensor2pil = transforms.ToPILImage()
        self.to_tensor = transforms.ToTensor()

        self.psnr = PSNR()
        self.ssim = SSIM()
        self.mae = MeanAbsoluteError()
        self.mse = MeanSquaredError()
        self.rmse = self._rmse
        self.metrics_dict = {
            "PSNR": self.psnr,
            "SSIM": self.ssim,
            "MAE": self.mae,
            "MSE": self.mse,
            "RMSE": self._rmse
        }

    def _rmse(self, preds: Tensor, target: Tensor) -> Tensor:
        return torch.sqrt(self.mse(preds, target))

    def _compute_metrics(self, sr: Tensor, hr: Tensor) -> Dict[str, float]:
        results = {}
        for k, v in self.metrics_dict.items():
            results[k] = v(sr, hr)

        return results

    def forward(self, x):
        with torch.no_grad():
            return self.model(x).clamp(0.0, 1.0)

    def run_test(self, hr_image: Image) -> Tuple[Image, Image, Image, Dict[str, Dict[str, float]]]:
        hr_w, hr_h = hr_image.size

        w_mod = hr_w % self.upscale_factor
        h_mod = hr_h % self.upscale_factor

        if w_mod != 0:
            hr_image = fromarray(np.array(hr_image)[:, :-w_mod])
            hr_w, hr_h = hr_image.size
        if h_mod != 0:
            hr_image = fromarray(np.array(hr_image)[:-h_mod, :])
            hr_w, hr_h = hr_image.size

        downscale = transforms.Resize(
            (hr_h // self.upscale_factor, hr_w // self.upscale_factor),
            interpolation=transforms.InterpolationMode.BICUBIC
        )
        upscale = transforms.Resize(
            (hr_h, hr_w),
            interpolation=transforms.InterpolationMode.BICUBIC
        )
        lr_image = downscale(hr_image)
        sr_cubic = upscale(lr_image)

        preds = self.forward(self.model.preprocess_input(lr_image))
        sr_image = self.model.postprocess_output(preds, lr_image)

        metrics_cubic = self._compute_metrics(
            self.to_tensor(sr_cubic).to(self.device).unsqueeze(0),
            self.to_tensor(hr_image).to(self.device).unsqueeze(0)
        )
        metrics_sr = self._compute_metrics(
            self.to_tensor(sr_image).to(self.device).unsqueeze(0),
            self.to_tensor(hr_image).to(self.device).unsqueeze(0)
        )

        return lr_image, sr_cubic, sr_image, {"cubic": metrics_cubic, self.model_name: metrics_sr}

    def run_inference(self, image: Image) -> Image:
        lr = self.model.preprocess_input(image).to(self.device)
        sr = self.forward(lr)
        sr = self.model.postprocess_output(sr, image)
        return sr
