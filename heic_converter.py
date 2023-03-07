import argparse

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def open_n_save(path, format="JPEG"):
    path_not_suffix = path.split(".")[0]

    image = Image.open(path)
    image.save(f"{path_not_suffix}.{format}", format)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="path to the .heic image",
    )
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        help="image format to convert to",
    )

    args = parser.parse_args()

    if args.format:
        open_n_save(args.path, args.format.upper())
    else:
        open_n_save(args.path)
