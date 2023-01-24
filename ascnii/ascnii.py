"""View brain images in terminal using ASCII characters."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

import tempfile
import warnings
from pathlib import Path

import ascii_magic
from nilearn import datasets, image, plotting

from .args import parse_args
from .utils import (get_background_color, get_input_params,
                    get_output_function, get_output_type)


def main():
    """Run main program."""
    args = parse_args()
    img = image.load_img(args.nifti)
    header = img.header
    if img.ndim == 4:
        img = image.mean_img(img)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        mask = datasets.load_mni152_brain_mask()

    mask = image.resample_to_img(mask, img, interpolation="nearest")
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

        output_type = get_output_type(args.output)
        input_params = get_input_params(output_type)

        img_ascii = ascii_magic.from_image_file(
            tmp / "plot.png",
            columns=args.columns,
            back=get_background_color(args.background),
            width_ratio=args.widthratio,
            **input_params,
        )

        out_func = get_output_function(output_type)
        out_func(args.output, img_ascii)

        if args.header:
            print(header)
