# -*- coding: utf-8 -*-
# Model names
SRCNN = "srcnn"

models = [
    SRCNN,
]

# Model configurations
srcnn_config = {
    "num_channels": 1,
}

configs = {
    SRCNN: srcnn_config,
}

# Possible model upscale factors
model_upscale_factors = {
    SRCNN: ["2x", "3x", "4x"],
}

# Possible model versions
model_versions = {
    SRCNN: None,
}
