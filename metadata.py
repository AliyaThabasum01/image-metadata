import os
from PIL import Image


def get_metadata(path):
    if not os.path.isfile(path):
        return None

    try:
        image = Image.open(path)

        return {
            "File": os.path.basename(path),
            "Format": image.format,
            "Width": image.width,
            "Height": image.height,
            "Mode": image.mode,
            "Size": f"{os.path.getsize(path) / 1024:.2f} KB"
        }

    except Exception:
        return None
