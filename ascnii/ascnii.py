"""View brain images in terminal using ASCII characters."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

import tempfile
from pathlib import Path

import ascii_magic
from nilearn import datasets, image, plotting

import warnings

from .args import parse_args


def get_background_color(color_string):
    """Get background color object for ascii_magic from string."""
    colors = {
        "black": ascii_magic.Back.BLACK,
        "red": ascii_magic.Back.RED,
        "green": ascii_magic.Back.GREEN,
        "yellow": ascii_magic.Back.YELLOW,
        "blue": ascii_magic.Back.BLUE,
        "magenta": ascii_magic.Back.MAGENTA,
        "cyan": ascii_magic.Back.CYAN,
        "white": ascii_magic.Back.WHITE,
    }

    return colors[color_string]


def main():
    """Run main program."""
    args = parse_args()
    img = image.load_img(args.nifti)
    header = img.header
    if img.ndim == 4:
        img = image.mean_img(img)
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        mask = datasets.load_mni152_template()
    
    mask = image.resample_to_img(mask, img)
    img = image.math_img("img * mask", img=img, mask=mask)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        img_plotted = plotting.plot_img(
            img,
            cut_coords=tuple(args.cut_coords),
            resampling_interpolation="nearest",
            colorbar=args.colorbar,
            black_bg=True,
            threshold=args.threshold,
            annotate=args.annotate,
            draw_cross=args.draw_cross,
            cbar_tick_format="%i",
            cmap=args.colormap,
        )

        img_plotted.savefig(tmp / "plot.png")
        img_ascii = (
            ascii_magic.from_image_file(
                tmp / "plot.png",
                columns=args.columns,
                back=get_background_color(args.background),
            )
            .replace(")", " ")
            .replace("=", " ")
        )
        ascii_magic.to_terminal(img_ascii)
        if args.header:
            print(header)
