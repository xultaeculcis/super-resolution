import torch

from app.inference.models.sr_base import SuperResolutionBaseModel
from app.inference import model_configs
from app.inference.models.srcnn import SRCNN
from app.inference.model_configs import configs

model_lookup = {
    "srcnn-2x": "./weights/srcnn_x2.pth",
    "srcnn-3x": "./weights/srcnn_x3.pth",
    "srcnn-4x": "./weights/srcnn_x4.pth",
}


def load_model(model_name: str, scaling_factor: int, model_version: str) -> SuperResolutionBaseModel:
    key = f"{model_name}-{scaling_factor}x"
    if model_version:
        key = key + model_version

    model_path = model_lookup[key]

    if model_name == model_configs.SRCNN:
        config = configs[model_configs.SRCNN].copy()
        config["upscale_factor"] = scaling_factor

        model = SRCNN(**config)
    else:
        raise ValueError(f"Model '{model_name}' is not supported. Supported models: {model_configs.models}")

    state_dict = model.state_dict()
    for n, p in torch.load(model_path, map_location=lambda storage, loc: storage).items():
        if n in state_dict.keys():
            state_dict[n].copy_(p)
        else:
            raise KeyError(n)

    model.eval()

    return model
