from PIL import Image
import os
from glob import glob
from tqdm import tqdm


def run():
    src_image_path = "../app/assets/image-enhancement/original"
    output_path_lr = "../app/assets/image-enhancement/lr"
    output_path_hr = "../app/assets/image-enhancement/hr"
    output_path_upscaled = "../app/assets/image-enhancement/upscaled"
    src_images = glob(os.path.join(src_image_path, "*.png"))
    crop_h, crop_w = (128, 128)
    scaling_factor = 4

    for src_image_path in tqdm(src_images):
        basename = os.path.basename(src_image_path)
        hr = Image.open(src_image_path)

        h, w = hr.size

        left = (w - crop_w) / 2
        top = (h - crop_h) / 2
        right = (w + crop_w) / 2
        bottom = (h + crop_h) / 2

        crop = hr.crop((left, top, right, bottom))
        crop.save(os.path.join(output_path_hr, f"HR-{basename}"))

        lr = crop.resize((crop_h // scaling_factor, crop_w // scaling_factor), Image.BICUBIC)
        lr.save(os.path.join(output_path_lr, f"LR-{basename}"))

        for filter, filter_name in [
            (Image.NEAREST, "NEAREST"),
            (Image.BICUBIC, "BICUBIC"),
            (Image.BILINEAR, "BILINEAR"),
            (Image.LANCZOS, "LANCZOS"),
            (Image.BOX, "BOX"),
            (Image.HAMMING, "HAMMING"),
        ]:
            upscaled = lr.resize((crop_h, crop_w), filter)
            upscaled.save(os.path.join(output_path_upscaled, f"{filter_name}-{basename}"))


if __name__ == '__main__':
    run()
